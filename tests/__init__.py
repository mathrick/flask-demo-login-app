from flask import Flask
from config import TestConfig
from app import app, db
from flask.ext.testing import TestCase

class FlaskTestCase(TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
    def create_app(self):
        app.config.from_object(TestConfig)
        db.init_app(app)
        return app

