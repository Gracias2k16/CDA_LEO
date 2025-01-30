from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector
import bcrypt
from app import app
from app.forms import ConfigForm

#===================================================================================================

@app.route('/Connexion', methods=['GET', 'POST'])
def login_form():

#    if request.method == 'POST':
        
 #       identifiant = request.form['identifiant']# Récupérer les données du formulaire
  #      password = request.form['password']# Récupérer les données du formulaire

   #     if validate_user(identifiant, password):
    #        return redirect(url_for('home'))  # Redirection si le mot de passe est correct
        
     #   else:
      #      flash("Identifiant ou mot de passe incorrect.")
       #     return redirect(url_for('home.html'))

    return render_template('Connexion.html')


#===================================================================================================

@app.route('/')
def home():
    return render_template('home.html')

#===================================================================================================

@app.route('/Demande')
def Demande():
    return render_template('Demande.html')
