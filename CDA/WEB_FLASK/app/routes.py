from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector
import bcrypt
from app import app
from app.forms import ConfigForm

#===================================================================================================

def connect_db():
    config = {
        'user': 'root',
        'password': 'uimm',  # Utilise le bon mot de passe ici
        'host': 'localhost',
        'database': 'CDA'
    }
    return mysql.connector.connect(**config)

#===================================================================================================

@app.route('/', methods=['GET', 'POST'])
def login_form():
    connexion = None  # Initialisation de la variable connexion

    if request.method == 'POST':
        # Récupérer les données du formulaire
        identifiant = request.form['identifiant']
        password = request.form['password']

    try:
            # Connexion à la base de données
            connexion = connect_db()
            mycursor = connexion.cursor()

            # Requête SQL pour récupérer l'utilisateur avec cet identifiant
            query = "SELECT Identifiant, Mot_de_passe FROM Utilisateurs WHERE Identifiant = %s"
            mycursor.execute(query, (identifiant,))
            user_data = mycursor.fetchone()

            if user_data:
                identifiant_bdd, password_bdd = user_data  # Récupérer l'identifiant et le mot de passe

                # Comparer le mot de passe saisi avec celui stocké dans la base
                if password == password_bdd:
                    return redirect(url_for('home'))  # Redirection si le mot de passe est correct
                else:
                    flash("Mot de passe incorrect.")
            else:
                flash("Identifiant incorrect.")

    except:
            flash(f"Erreur lors de la connexion ")

    finally:
        if connexion:
            connexion.close()
    return render_template('form_config.html')



#===================================================================================================

@app.route('/home')
def home():
    return "<h1>Bienvenue à la maison !</h1>"

