from flask import render_template, url_for, redirect, flash
from app import db, app, forms, models, bcrypt
from flask.ext.login import login_user
from sqlalchemy.exc import IntegrityError
from app.decorators import json_result

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        u = authenticate_user(form)
        if u:
            flash("You have been successfully logged in", "success")
            return redirect(url_for('index'))
        flash("Invalid email or password", "danger")
    return render_template("login.html", form=form)
    
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

def make_new_user(form):
    u = models.User(name=form.name.data,
                    email=form.email.data,
                    pw_hash=bcrypt.generate_password_hash(form.password.data))
    db.session.add(u)
    db.session.commit()

def authenticate_user(form):
    return models.User.query.filter_by(email=form.email.data).first()
        
    
@app.route('/api/test')
@json_result
def api_test():
    return {"message": "My hovercraft is full of eels"}
