from . import FlaskTestCase
from app.models import User, Message

class TestUser(FlaskTestCase):
    def test_no_users_in_empty_db(self):
        # This mostly serves as a sanity check for when we mess
        # something up in SQLAlchemy mappings, etc. We obviously
        # expect to have no users in an empty DB, but just trying the
        # query will catch some classes of errors simply defining the
        # models will not
        self.assertEqual(0, len(User.query.all()))
        
class TestMessage(FlaskTestCase):
    def test_no_messages_in_empty_db(self):
        self.assertEqual(0, len(Message.query.all()))
