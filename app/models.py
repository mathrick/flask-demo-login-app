from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True)
    email = db.Column(db.String(100), index = True, unique = True)
    pw_hash = db.Column(db.String(60), index = True)
    messages = db.relationship('Message', backref = 'recipient', lazy = 'dynamic')
    
    def __repr__(self):
        return "<User %s>" % self.name

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), index = True)
    text = db.Column(db.Text)

    timestamp = db.Column(db.DateTime, server_default = db.func.current_timestamp())
    unread = db.Column(db.Boolean, default = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
