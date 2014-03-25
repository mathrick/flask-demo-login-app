from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, Email

class SignUpForm(Form):
    name = TextField('name', validators=[Required])
    email = EmailField('email', validators=[Required, Email])
    password = PasswordField('password', validators=[Required])
