from flask import request, render_template, flash, redirect, url_for, session
import mysql.connector
from app import app
from app.Fonctions_BDD import connexion_à_BDD, Recupération_des_utilisateurs
from app.__init__ import bcrypt
import mysql
from flask import jsonify

#===================================================================================================

@app.route('/Connexion', methods=["GET", "POST"])
def Connexion():
    if request.method == 'POST':
        email = request.form['identifiant']
        password = request.form['password']

        user = Recupération_des_utilisateurs(email)  # Récupère l'utilisateur en BDD

        if user and bcrypt.check_password_hash(user['id_Mdp'], password):  # Vérifie le mot de passe
            session['user_id'] = user['id_Utilisateur']
            session['email'] = user['id_Mail']
            flash(f"Bienvenue, {user['id_Mail']} !", 'success')
            return redirect(url_for('home'))
        else:
            flash("Identifiant ou mot de passe incorrect.", 'danger')

    return render_template ('Connexion.html')

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
def Creation_compte():
    if request.method == 'GET':
        return render_template('Creation_compte.html')  # Affiche la page HTML avec le formulaire

    elif request.method == 'POST':
        data = request.form  # Récupère les données envoyées par le formulaire

    required_fields = ["Nom", "Mail","Mdp", "Num"] # Champs requis
    if not all(field in data and data[field] for field in required_fields):
        flash("Certains champs obligatoires sont manquants.", 'danger')
        return redirect(url_for('Creation_compte')) #Erreur si tous els champs ne sont pas compéltés

    nom = data["Nom"]
    prenom = data.get("Prenom", "")  # Optionnel
    societe = data.get("Sociétée", "")  # Optionnel
    mail = data["Mail"]
    mot_de_passe = data["Mdp"]
    num = data["Num"]

    hashed_password = bcrypt.generate_password_hash(mot_de_passe).decode('utf-8')

    conn, cur = connexion_à_BDD()  # Connexion à la BDD
    if conn is None or cur is None:
        flash("Impossible de se connecter à la base de données.", 'danger')
        return redirect(url_for('Creation_compte'))
    
    try:
        cur.execute("SELECT * FROM Compte WHERE id_Mail = %s", (mail,))# Vérifier si l'email existe déjà
        if cur.fetchone():
            flash("Cet email est déjà utilisé.", 'danger')
            return redirect(url_for('Creation_compte'))

        sql = "INSERT INTO Compte (id_Nom, id_Prenom, id_Nom_societee, id_Mail, id_Mdp, Num_tel, id_Type) VALUES (%s, %s, %s, %s, %s, %s, %s)" #requete sql pour inseré le compte
        cur.execute(sql, (nom, prenom, societe, mail, hashed_password, num, 'USER'))
        conn.commit()

        flash("Compte créé avec succès !", 'success')
        return redirect(url_for('Creation_compte'))

    except mysql.connector.Error as e:
        conn.rollback()
        flash(f"Erreur lors de la création du compte : {str(e)}", 'danger')
        return redirect(url_for('Creation_compte'))

    finally:
        cur.close()
        conn.close()

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