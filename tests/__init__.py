from app import app
from unittest import TestCase

class FlaskTestCase(TestCase):
    def setUp(self):
        self.client = app.test_client()
    def tearDown(self):
        pass
