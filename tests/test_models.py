from . import FlaskTestCase
from unittest import skip, skipIf
from app import db
from app.models import User, Message

class TestUser(FlaskTestCase):
    def test_no_users_in_empty_db(self):
        # This mostly serves as a sanity check for when we mess
        # something up in SQLAlchemy mappings, etc. We obviously
        # expect to have no users in an empty DB, but just trying the
        # query will catch some classes of errors simply defining the
        # models will not
        self.assertEqual(0, len(User.query.all()))

    def test_create_user(self):
        db.session.add(User(name = "King Arthur", email = "arthur@camelot.org"))
        db.session.add(User(name = "Sir Lancelot", email = "lancelot@camelot.org"))
        db.session.commit()

        self.assertEqual(2, len(User.query.all()))

class TestMessage(FlaskTestCase):
    def setUp(self):
        super(TestMessage,self).setUp()
        db.session.add(User(name = "King Arthur", email = "arthur@camelot.org"))
        db.session.add(User(name = "Sir Lancelot", email = "lancelot@camelot.org"))
        db.session.commit()
        
    
    def test_no_messages_in_empty_db(self):
        self.assertEqual(0, len(Message.query.all()))

    def test_make_welcome_message(self):
        pass
        arthur = User.query.filter_by(name = "King Arthur").first()
        db.session.add(Message(recipient = arthur,
                               title = "Welcome!",
                               text = "Hello, %s!\nWelcome to zombo.com" % arthur.name))
        
        db.session.commit()

        self.assertEqual(1, len(Message.query.all()))
        self.assertEqual(1, len(Message.query.filter_by(recipient = arthur).all()))
