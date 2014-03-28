from app import app, models, db
from functools import wraps
from flask.ext.restful import Api, Resource, fields, reqparse, marshal_with, abort
from flask.ext.login import current_user, login_required

def api_login_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if app.login_manager._login_disabled or \
           current_user.is_authenticated():
            return func(*args, **kwargs)
        else:
            abort(403, message="User not authenticated")
    return decorated

def valid_recipient(email):
    recipient = models.User.query.filter_by(email=email).first()
    if not recipient:
        raise ValueError("Invalid recipient email: {}".format(email))
    
message_list_fields = { 'id': fields.Integer,
                        'title': fields.String,
                        'unread': fields.Boolean,
                        'text': fields.String,
                        'timestamp': fields.DateTime,
                    }

message_parser = reqparse.RequestParser()
message_parser.add_argument('title', type=str, required=True)
message_parser.add_argument('text', type=str, required=True)
message_parser.add_argument('recipient', type=str, required=valid_recipient)

class MessageList(Resource):
    @api_login_required
    @marshal_with(message_list_fields)
    def get(self):
        return models.Message.query.filter_by(recipient=current_user).all()

    def post(self):
        data = message_parser.parse_args()
        recipient = models.User.query.filter_by(email=data['recipient']).first()
        if not recipient:
            abort(400, message="Invalid recipient email")
        message = models.Message(title=data['title'],
                                 text=data['text'],
                                 recipient=recipient)
        db.session.add(message)
        db.session.commit()

unread_parser = reqparse.RequestParser()
unread_parser.add_argument('unread', type=bool, required=True)
        
class Message(Resource):
    @api_login_required
    @marshal_with(message_list_fields)
    def get(self, id):
        message = models.Message.query.get(id)
        if not message:
            abort(404, message="Invalid message id")
        if message.recipient == current_user:
            message.unread = False
            db.session.commit()
            return message
        else:
            abort(403)

    @api_login_required
    def put(self, id):
        data = unread_parser.parse_args()
        message = models.Message.query.get(id)
        message.unread = data['unread']
        db.session.commit()

class UserList(Resource):
    @api_login_required
    def get(self):
        return {user.email: user.name for
                user in models.User.query.all()}

api = Api(app)
api.add_resource(MessageList, '/api/message/', endpoint='api_message_list')
api.add_resource(Message, '/api/message/<int:id>', endpoint='api_message')
api.add_resource(UserList, '/api/users/', endpoint='api_user_list')
