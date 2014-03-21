from flask import render_template
from app import app
from app.decorators import json_result

@app.route('/')
@json_result
def index():
    return {"message": "My hovercraft is full of eels"}
