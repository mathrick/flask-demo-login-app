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

angular_syntax = {
    'block_start_string': '{{{%',
    'block_end_string': '%}}}',
    'variable_start_string': '{{{',
    'variable_end_string': '}}}',
    'comment_start_string': '{{{#',
    'comment_end_string': '}}}',
}

app.angular_env = app.jinja_env.overlay(**angular_syntax)

from app import views, models, forms, api

app.jinja_env.globals['get_unread_count'] = views.get_unread_count
