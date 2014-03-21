from flask import render_template
from app import app

@app.route('/')
def index():
    return "My hovercraft is full of eels"
