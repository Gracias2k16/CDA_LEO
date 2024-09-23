from flask import render_template, redirect
from app import app
from app.forms import ConfigForm

@app.route('/') # decorators
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    strResult = f'Hello Bruz! '
    return strResult

@app.route('/config', methods=['GET', 'POST'])
def config():
    form = ConfigForm(Identifiant= "ZEBI", MDP="123456")
    if form.validate_on_submit():
        return redirect('/')
    return render_template('form_config.html', form=form)
