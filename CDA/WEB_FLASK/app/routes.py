from flask import request, render_template, flash, redirect, url_for, session
import mysql.connector
from app import app
from app.Model import connexion_à_BDD, gerer_comptes_Fonction, Connexion_utilisateur, Création_Compte
import mysql
from flask import jsonify


#===================================================================================================

@app.route('/Connexion', methods=["GET", "POST"])
def Connexion():
    return Connexion_utilisateur();

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
    return Création_Compte();
    
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

    if 'user_id' not in session: # Vérifier si l'utilisateur est connecté
        flash("Vous devez être connecté pour accéder à cette page.", "warning")
        return redirect(url_for('Connexion'))

    if session.get('role') != 'ADMIN':  # Vérifier si l'utilisateur est ADMIN
        flash("Accès refusé : Vous n'avez pas les droits d'administration.", "danger")
        return redirect(url_for('home'))

    conn, cur = connexion_à_BDD() 
    if conn is None or cur is None:
        return render_template('Comptes.html', users=[])

    try:
        cur.execute("SELECT id_Mail, id_Type FROM  Compte")
        users = cur.fetchall()
        return render_template('Comptes.html', users=users)
    
    except mysql.connector.Error as err:
        print(f"Erreur lors de la récupération : {err}")
        return render_template('Comptes.html', users=[])
    
    finally:
        cur.close()
        conn.close()

#===================================================================================================

@app.route('/gerer_comptes', methods=['POST'])
def gestion_compte():
    return gerer_comptes_Fonction();
