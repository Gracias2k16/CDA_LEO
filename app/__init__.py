from flask import Flask
import os
from flask_mail import Mail
from flask_wtf import CSRFProtect
from app.Setting import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_USERNAME
import mysql.connector

app = Flask(__name__)
csrf = CSRFProtect(app)
mail = Mail(app)

# Configuration de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Utilisez le serveur SMTP de votre choix
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'Adressemail'  # Remplacez par votre adresse e-mail
app.config['MAIL_PASSWORD'] = 'Adressemail_MDP'  # Remplacez par votre mot de passe
app.config['MAIL_DEFAULT_SENDER'] = 'Adressemail'  # Adresse d'envoi

# Configuration de la clé secrète
app.secret_key = os.urandom(24)

# Configuration des cookies de session
app.config['SESSION_COOKIE_SAMESITE'] = 'None'  # ou 'Lax' ou 'Strict' selon vos besoins
app.config['SESSION_COOKIE_SECURE'] = True  # Assurez-vous que votre site utilise HTTPS

# Importer les routes après la configuration
from app import routes

#Connexion a la base de données
def connexion_à_BDD():
    try:
        conn = mysql.connector.connect(# Connexion à la base de données
        host= DB_HOST,
        user= DB_USERNAME,
        password= DB_PASSWORD,
        database= DB_DATABASE
        )

        if conn.is_connected():
            print("Connecté à la BDD")
        cur = conn.cursor()  # Création du curseur
        return conn, cur
        
    except mysql.connector.Error as err:
        print(f"erreur de connexion : {err}")
        return None, None 