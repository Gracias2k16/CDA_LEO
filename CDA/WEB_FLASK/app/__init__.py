from flask import Flask, session
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
bcrypt = Bcrypt(app)

# Configuration de la clé secrète
app.secret_key = os.urandom(24)

# Configuration des cookies de session
app.config['SESSION_COOKIE_SAMESITE'] = 'None'  # ou 'Lax' ou 'Strict' selon vos besoins
app.config['SESSION_COOKIE_SECURE'] = True  # Assurez-vous que votre site utilise HTTPS

# Importer les routes après la configuration
from app import routes