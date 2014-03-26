from flask import render_template, url_for, redirect
from app import db, app, forms, models
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
        make_new_user(form)
        return redirect(url_for('index'))
    return render_template("sign-up.html", form=form)

def make_new_user(form):
    pass

@app.route('/api/test')
@json_result
def api_test():
    return {"message": "My hovercraft is full of eels"}
