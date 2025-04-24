from flask import render_template, flash, redirect, url_for, session
from app import app
from app.Model import gerer_comptes_Fonction, Connexion_utilisateur, Création_Compte, acces_comptes
from flask import jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

#===================================================================================================

@app.after_request
def add_security_headers(response):
    response.headers["Content-Security-Policy"] = (
        "img-src 'self' data:; "
        "font-src 'self' https://fonts.gstatic.com; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "frame-ancestors 'none'; "
        "connect-src 'self'; "
        "form-action 'self';"
    )
    return response

#===================================================================================================

@app.route('/Connexion', methods=["GET", "POST"])
def Connexion():
    return Connexion_utilisateur()

#===================================================================================================

@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html')


#===================================================================================================

@app.route('/Demande',methods=['GET', 'POST'])
def Demande_route():
    return render_template('Demande.html')

#===================================================================================================

@app.route('/Creation_compte', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def Creation_compte_route():
    return Création_Compte()
    
#===================================================================================================

@app.route('/session-data')
def session_data():
    return jsonify(dict(session))

#===================================================================================================

@app.route('/logout')
def logout():
    session.clear()
    flash("Déconnexion réussie.", "success")
    return redirect(url_for('Connexion'))

#===================================================================================================

@app.route('/Comptes')
def Comptes():
    return acces_comptes()

#===================================================================================================

@app.route('/gerer_comptes', methods=['POST'])
def gestion_compte():
    return gerer_comptes_Fonction()

#===================================================================================================
