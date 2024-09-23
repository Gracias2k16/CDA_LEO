from flask import render_template
from app import app

@app.route('/') # decorators
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    strResult = f'Hello Bruz! '
    return strResult