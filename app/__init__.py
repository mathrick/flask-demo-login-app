from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)

from app import views, models
