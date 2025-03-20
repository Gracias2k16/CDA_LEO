from flask import render_template, flash, redirect, url_for, session
from app import app
from app.Model import gerer_comptes_Fonction, Connexion_utilisateur, Création_Compte, acces_comptes
from flask import jsonify


#===================================================================================================

@app.route('/Connexion', methods=["GET", "POST"])
def Connexion():
    return Connexion_utilisateur()

#===================================================================================================

@app.route('/')
def home():
    return render_template('home.html')

#===================================================================================================

@app.route('/Demande')
def Demande():
    return render_template('Demande.html')

#===================================================================================================

@app.route('/Creation_compte', methods=['GET', 'POST'])
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
