from . import FlaskTestCase
from app import db
from app.models import User, Message
from datetime import datetime, timedelta

# These tests are necessarily very rudimentary, as the application and
# its models do very little, so we're mostly testing SQLAlchemy. But
# that is still valuable, as it serves to make sure we're using
# SQLAlchemy properly (it's a really flexible package and it's easy to
# do something you're not supposed to) and at the same time, or that
# we don't have something specific to the RDBMS used when porting to
# another one

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
        arthur = User.query.filter_by(name = "King Arthur").first()
        timestamp = datetime.utcnow()

        db.session.add(Message(recipient = arthur,
                               title = "Welcome!",
                               text = "Hello, %s!\nWelcome to zombo.com" % arthur.name))
        db.session.commit()

        self.assertEqual(1, len(Message.query.all()))
        self.assertEqual(1, len(Message.query.filter_by(recipient = arthur).all()))

        msg = Message.query.filter_by(recipient = arthur).first()
        self.assertTrue(msg.unread)
        # Give up to two seconds of leeway in timestamps, as utcnow()
        # only operates on second precision
        self.assertLessEqual(abs(msg.timestamp - timestamp), timedelta(0,2))
