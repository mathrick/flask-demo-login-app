from flask import render_template, url_for, redirect, request, flash, abort
from app import db, app, forms, models, api, bcrypt
from flask.ext.login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import IntegrityError
from app.decorators import json_result
import random

@app.route('/')
def index():
    user = None
    if current_user.is_authenticated():
        user = current_user
    return render_template("index.html", user=user)

app.login_manager.login_view = "login"
@app.route('/login', methods=["GET", "POST"])
def login():
    form = forms.LoginForm()
    next_url = request.args.get('next', url_for('index'))
    if form.validate_on_submit():
        u = authenticate_user(form)
        if u:
            flash("You have been successfully logged in", "success")
            login_user(u)
            return redirect(next_url)
        flash("Invalid email or password", "danger")
    return render_template("login.html", form=form, next_url=next_url)

@app.route('/logout')
def logout():
    if current_user.is_authenticated():
        logout_user()
        flash("You have been logged out", "info")
    return redirect(url_for('index'))


@app.route('/populate-users', endpoint='populate-users')
def make_some_users():
    # For debug purposes only
    users = [('King Arthur', 'arthur@camelot.org'),
             ('Sir Lancelot', 'lancelot@camelot.org'),
             ('Sir Robin', 'robinthebrave@camelot.org'),
    ]
    for name, email in users:
        if not models.User.query.filter_by(email=email).first():
            db.session.add(models.User(name=name, email=email,
                                       pw_hash=bcrypt.generate_password_hash('asd')))
    db.session.commit()

    users = models.User.query.all()
    return render_template("users.html", users=users)

@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    form = forms.SignUpForm()
    if form.validate_on_submit():
        try:
            make_new_user(form)
            flash("You have been successfully registered", "success")
            return redirect(url_for('index'))
        except IntegrityError:
            form.email.errors += ['This email has been registered already']
    return render_template("sign-up.html", form=form)

@login_required
@app.route('/message/')
@app.route('/inbox/')
def inbox():
    messages = api.MessageList().get()
    return render_template('inbox.html', user=current_user, messages=messages)

@login_required
@app.route('/message/<int:id>')
def message(id):
    if not id:
        return redirect(url_for('inbox'))
    message = models.Message.query.get(id)
    if not message:
        abort(404)
    if message.recipient != current_user:
        return app.login_manager.unauthorized()
    message.unread = False
    db.session.commit()
    return render_template('message.html', message=message, user=message.recipient)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404
    
def send_welcome_message(user):
    messages = ["My hovercraft is full of eels",
                "African swallow is bigger than European swallow",
                "We are the Knight Who Say Ni"
            ]
    db.session.add(models.Message(recipient=user,
                                  title="Welcome!",
                                  text=random.choice(messages)))

def get_unread_count():
    if current_user.is_authenticated():
        return models.Message.query.filter_by(recipient=current_user, unread=True).count()

def make_new_user(form):
    u = models.User(name=form.name.data,
                    email=form.email.data,
                    pw_hash=bcrypt.generate_password_hash(form.password.data))
    db.session.add(u)
    send_welcome_message(u)
    db.session.commit()

def authenticate_user(form):
    u = models.User.query.filter_by(email=form.email.data).first()
    return u if bcrypt.check_password_hash(u.pw_hash, form.password.data) else None
        
    
@app.route('/api/test')
@json_result
def api_test():
    return {"message": "My hovercraft is full of eels"}
