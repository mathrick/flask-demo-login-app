from flask import Flask
from config import TestConfig
from app import app, db
from flask.ext.testing import TestCase

class FlaskTestCase(TestCase):
    def create_app(self):
        app.config.from_object(TestConfig)
        db.init_app(app)
        return app

