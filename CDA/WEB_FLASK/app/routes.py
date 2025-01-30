from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector
import bcrypt
from app import app
from app.forms import ConfigForm

#===================================================================================================


def connect_db():
    config = {
        'user': 'root',
        'password': 'uimm', 
        'host': 'localhost',
        'database': 'CDA'
    }
    return mysql.connector.connect(**config)

#===================================================================================================



def fetch_user_data(identifiant): #Récupère les données de l'utilisateur à partir de la base de données
    connexion = connect_db()
    mycursor = connexion.cursor()

    try:
        query = "SELECT Identifiant, Mot_de_passe FROM Utilisateurs WHERE Identifiant = %s"
        mycursor.execute(query, (identifiant,))
        
        return mycursor.fetchone()  # Renvoie les données de l'utilisateur
    

    except :
        print("Erreur lors de la récupération des données")
        return None
    

    finally:
        mycursor.close()
        connexion.close()


#===================================================================================================


def validate_user(identifiant, password):#Valide l'identifiant et le mot de passe de l'utilisateur
    
    user_data = fetch_user_data(identifiant)
    if user_data:

        identifiant, password_bdd = user_data  # Récupérer l'identifiant et le mot de passe

        if password == password_bdd:# Comparer le mot de passe saisi avec celui stocké dans la base
            return redirect(url_for('home'))  # Redirection si le mot de passe est correct
        
        else:
            flash("Mot de passe incorrect.")

    else:
        flash("Identifiant incorrect.")

    return False  # Validation échouée


#===================================================================================================

@app.route('/Connexion', methods=['GET', 'POST'])
def login_form():

    if request.method == 'POST':
        
        identifiant = request.form['identifiant']# Récupérer les données du formulaire
        password = request.form['password']# Récupérer les données du formulaire

        if validate_user(identifiant, password):
            return redirect(url_for('home'))  # Redirection si le mot de passe est correct
        
        else:
            flash("Identifiant ou mot de passe incorrect.")
            return redirect(url_for('home.html'))

    return render_template('Connexion.html')


#===================================================================================================

@app.route('/')
def home():
    return render_template('home.html')

#===================================================================================================

@app.route('/Demande')
def Demande():
    return render_template('Demande.html')
