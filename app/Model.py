import mysql.connector
from app.Setting import Email_MDP, Email
from app.__init__ import connexion_à_BDD
import smtplib
from email.message import EmailMessage
from flask import request, flash, redirect, url_for, render_template, session
from app import bcrypt

#===================================================================================================

def Recupération_des_utilisateurs(email):
    conn, cur = connexion_à_BDD() 
    if conn is None or cur is None:
        return None  

    try:
        query = "SELECT id_Utilisateur, id_Mail, id_Mdp, id_Type FROM Compte WHERE id_Mail = %s" #sql qui permet de récupérer l'email
        cur.execute(query, (email,)) 

        user = cur.fetchone() #Stock l'adersse mail 

        if user:
            return {'id_Utilisateur': user[0], 'id_Mail': user[1], 'id_Mdp': user[2], 'id_Type': user[3]}  # Retournez un dictionnaire avec les informations
        return None
    except mysql.connector.Error as err:
        print(f"Erreur lors de la récupération : {err}")
        return None
    finally:
        cur.close()
        conn.close()

#===================================================================================================

def Ecriture_adresse():
    conn, cur = connexion_à_BDD()
    try:
        conn, cur = connexion_à_BDD()
        if conn is None or cur is None:
            return
    
        sql = """INSERT INTO Adresse (id_N_Rue, id_CP, id_Cmplt_rue, id_Ville, id_Nom_rue)
                 VALUES (%s, %s, %s, %s, %s)"""
        
        # Valeurs à insérer
        values = (50, 35000, '', 'RENNES', 'Rue des Résistants')

        # Exécution de la requête
        cur.execute(sql, values)
        conn.commit()

        print(f"{cur.rowcount} enregistrement inséré.")

    except mysql.connector.Error as err:
        print(f"Erreur lors de l'insertion : {err}")

    finally:
        # Fermeture du curseur et de la connexion
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

#===================================================================================================

def Envoie_mail_confirmation (mail):
    try:

        msg = EmailMessage()
        msg['Subject'] = 'Confirmation de création de compte'  # Sujet de l'e-mail
        msg['From'] = Email  # Adresse e-mail de l'expéditeur
        msg['To'] = mail
        print(mail)
    
        # Corps du message
        msg.set_content("Votre compte a été créé avec succès.\n\nMerci de nous avoir rejoints !\n\nCordialement,\nL'équipe.")


        server = smtplib.SMTP('smtp.gmail.com', 587)  
        server.starttls()
        server.login(Email, Email_MDP)
        #erver.sendmail(Email, mail, "Votre compte a ete cree avec succes")
        server.send_message(msg)  # Envoie le message
        server.quit()
        print("Email envoyé avec succès")
    except Exception as e:
        print(f"Erreur : {e}")

#===================================================================================================

def gerer_comptes_Fonction():
    conn, cur = connexion_à_BDD()

    try:
        selected_users = request.form.getlist('selected_users')
        action = request.form.get('action')

        print("Utilisateurs sélectionnés :", selected_users)
        print("Action demandée :", action)

        if not selected_users:
            flash("Aucun utilisateur sélectionné.", "danger")
            return redirect(url_for('Comptes'))

        if action == "modifier":
            for user_email in selected_users:
                new_role = request.form.get(f'new_role_{user_email}')
                if new_role:
                    cur.execute("UPDATE Compte SET id_Type = %s WHERE id_Mail = %s", (new_role, user_email))
            conn.commit()
            flash("Les rôles ont été modifiés avec succès.", "success")

        elif action == "supprimer":
            for user_email in selected_users:
                cur.execute("DELETE FROM Compte WHERE id_Mail = %s", (user_email,))
            conn.commit()
            flash("Les comptes ont été supprimés avec succès.", "success")

    except mysql.connector.Error as err:
        print(f"Erreur lors de l'opération : {err}")
        flash("Une erreur est survenue.", "danger")

    finally:
        cur.close()
        conn.close()

    return redirect(url_for('Comptes'))

#===================================================================================================

def Connexion_utilisateur():
    if request.method == 'POST':
        email = request.form['identifiant']
        password = request.form['password']

        user = Recupération_des_utilisateurs(email)  # Récupère l'utilisateur dans BDD

        if user and bcrypt.check_password_hash(user['id_Mdp'], password):  # Vérifie le mot de passe
            session['user_id'] = user['id_Utilisateur']
            session['email'] = user['id_Mail']
            session['role'] = user['id_Type']
            return redirect(url_for('home'))
        else:
            flash("Identifiant ou mot de passe incorrect.", 'danger')

    return render_template ('Connexion.html')

#===================================================================================================

def Création_Compte():
    if request.method == 'GET':
        return render_template('Creation_compte.html')  # Affiche la page HTML avec le formulaire

    elif request.method == 'POST':
        data = request.form  # Récupère les données envoyées par le formulaire

    required_fields = ["Nom", "Mail","Mdp", "Mdp_2","Num"] # Champs requis
    if not all(field in data and data[field] for field in required_fields):
        flash("Certains champs obligatoires sont manquants.", 'danger')
        return redirect(url_for('Creation_compte_route')) #Erreur si tous els champs ne sont pas compéltés

    nom = data["Nom"]
    prenom = data.get("Prenom", "")  # Optionnel
    societe = data.get("Sociétée", "")  # Optionnel
    mail = data["Mail"]
    mot_de_passe = data["Mdp"]
    mot_de_passe_confirmation = data["Mdp_2"]
    num = data["Num"]

    if mot_de_passe != mot_de_passe_confirmation:
            flash("Les mots de passe ne correspondent pas.", 'danger')
            return redirect(url_for('Creation_compte_route'))


    hashed_password = bcrypt.generate_password_hash(mot_de_passe).decode('utf-8')

    conn, cur = connexion_à_BDD()  # Connexion à la BDD
    if conn is None or cur is None:
        flash("Impossible de se connecter à la base de données.", 'danger')
        return redirect(url_for('Creation_compte_route'))
    
    try:
    # Vérifier si l'email existe déjà 
        cur.execute("SELECT * FROM Compte WHERE id_Mail = %s", (mail,))
        if cur.fetchone():
            flash("Cet email est déjà utilisé.", 'danger')
            return redirect(url_for('Creation_compte_route'))

        sql = """
        INSERT INTO Compte (id_Mail, Num_tel, id_Nom, id_Prenom, id_Nom_societee, id_Mdp, id_Type)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(sql, (mail, num, nom, prenom, societe, hashed_password, 'UTILISATEUR'))
        conn.commit()

        flash("Compte créé avec succès !", 'success')
    
        # Envoyer l'email de confirmation
        Envoie_mail_confirmation(mail)

        return redirect(url_for('Creation_compte_route'))

    except mysql.connector.Error as e:
        conn.rollback()
        flash(f"Erreur lors de la création du compte : {str(e)}", 'danger')
        return redirect(url_for('Creation_compte_route'))
    
#===================================================================================================

def acces_comptes():
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

#===================================================================================================

def Envoie_demadne():
    if request.method == 'GET':
        return render_template('Creation_compte.html')  # Affiche la page HTML avec le formulaire

    elif request.method == 'POST':
        data = request.form  # Récupère les données envoyées par le formulaire

        required_fields = ["marque", "serie", "moteur", "boite"]
        if not all(field in data and data[field].strip() for field in required_fields):
            flash("Certains champs obligatoires sont manquants.", 'danger')
    
    # Récupération des données
        marque = data["marque"]
        serie = data["serie"]
        moteur = data["moteur"]
        boite = data["boite"]
    
    # Connexion à la base de données
        conn, cur = connexion_à_BDD()
        if conn is None or cur is None:
            flash("Impossible de se connecter à la base de données.", 'danger')
    
    try:
            # Insertion des données dans la table
            sql = """
            INSERT INTO Demande (id_Marque, id_Serie, id_Moteur, id_Boite)
            VALUES (%s, %s, %s, %s)
            """
            cur.execute(sql, (marque, serie, moteur, boite))
            conn.commit()

            flash("Demande enregistrée avec succès !", 'success')

    except mysql.connector.Error as e:
            conn.rollback()
            flash(f"Erreur lors de l'enregistrement : {str(e)}", 'danger')