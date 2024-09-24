from flask import render_template, redirect
from app import app
from app.forms import ConfigForm

@app.route('/', methods=['GET', 'POST'])
def home():
    form = ConfigForm()
    if form.validate_on_submit('Connexion'):
        return redirect('/config')
    return render_template('form_config.html', form=form)

@app.route('/index')
def index():
    strResult = f'Hello Bruz!'
    return strResult

@app.route('/config',)
def config():
    return render_template('home.html')
