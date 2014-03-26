from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager, current_user

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
app.jinja_env.globals['static'] = lambda filename: url_for('static', filename = filename)
app.jinja_env.globals['get_authenticated_user'] = lambda: current_user if current_user.is_authenticated() else None

from app import views, models, forms
