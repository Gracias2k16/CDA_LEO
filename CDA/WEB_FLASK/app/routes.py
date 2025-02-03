from flask import Flask, request, render_template
from app import app

#===================================================================================================

@app.route('/Connexion', methods=["GET", "POST"])
def login_form():
    return render_template('Connexion.html')

#===================================================================================================

@app.route('/')
def home():
    return render_template('home.html')

#===================================================================================================

@app.route('/Demande')
def Demande():
    return render_template('Demande.html')
