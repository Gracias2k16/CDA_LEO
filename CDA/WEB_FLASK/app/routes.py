from flask import request, render_template, jsonify
from app import app
from app.Fonctions_BDD import connexion_à_BDD
from app.__init__ import bcrypt
import mysql

#===================================================================================================

@app.route('/Connexion', methods=["GET", "POST"])
def Connexion():
    return render_template('Connexion.html')

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
        return jsonify({"error": "Certains champs obligatoires sont manquants"}), 400 #Erreur si tous els champs ne sont pas compéltés

    nom = data["Nom"]
    prenom = data.get("Prenom", "")  # Optionnel
    societe = data.get("Sociétée", "")  # Optionnel
    mail = data["Mail"]
    mot_de_passe = data["Mdp"]
    num = data["Num"]

    hashed_password = bcrypt.generate_password_hash(mot_de_passe).decode('utf-8')

    conn, cur = connexion_à_BDD()  # Connexion à la BDD
    if conn is None or cur is None:
        return jsonify({"error": "Impossible de se connecter à la base de données"}), 500
    
    try:
        cur.execute("SELECT * FROM Compte WHERE id_Mail = %s", (mail,))# Vérifier si l'email existe déjà
        if cur.fetchone():
            return jsonify({"error": "Cet email est déjà utilisé"}), 400

        sql = "INSERT INTO Compte (id_Nom, id_Prenom, id_Nom_societee, id_Mail, id_Mdp, Num_tel) VALUES (%s, %s, %s, %s, %s, %s)" #requete sql pour inseré le compte
        cur.execute(sql, (nom, prenom, societe, mail, hashed_password, num))
        conn.commit()

        return jsonify({"message": "Compte créé avec succès !"}), 201

    except mysql.connector.Error as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        cur.close()
        conn.close()
        print(data)