from flask import render_template
from app import app
from app.decorators import json_result

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")
    
@app.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    return render_template("sign-up.html")
    
@app.route('/api/test')
@json_result
def api_test():
    return {"message": "My hovercraft is full of eels"}
