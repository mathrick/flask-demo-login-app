from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class SignUpForm(Form):
    name = TextField('name', validators=[DataRequired()])
    email = TextField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(),
                                                     EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('confirm password', validators=[DataRequired()])

class LoginForm(Form):
    email = TextField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('remember', default=False)
