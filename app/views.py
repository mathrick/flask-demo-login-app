from flask import render_template, url_for, redirect
from app import db, app, forms, models
from sqlalchemy.exc import IntegrityError
from app.password import bcrypt
from app.decorators import json_result

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template("login.html", form=form)
    
@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    form = forms.SignUpForm()
    if form.validate_on_submit():
        try:
            make_new_user(form)
            return redirect(url_for('index'))
        except IntegrityError:
            form.email.errors += ['This email has been registered already']
    return render_template("sign-up.html", form=form)

def make_new_user(form):
    u = models.User(name=form.name.data,
                    email=form.email.data,
                    pw_hash=bcrypt.generate_password_hash(form.password.data))
    db.session.add(u)
    db.session.commit()

@app.route('/api/test')
@json_result
def api_test():
    return {"message": "My hovercraft is full of eels"}
