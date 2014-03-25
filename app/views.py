from flask import render_template
from app import app
from app.decorators import json_result

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/test')
@json_result
def api_test():
    return {"message": "My hovercraft is full of eels"}
