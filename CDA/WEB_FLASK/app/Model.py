import mysql.connector
from app.Setting import Email_MDP, Email
from app.__init__ import connexion_à_BDD
import smtplib
from email.message import EmailMessage
from flask import request, flash, redirect, url_for, render_template, session
from app.__init__ import bcrypt

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

def Recuperation_tous_utilisateurs():
    conn, cur = connexion_à_BDD() 
    if conn is None or cur is None:
        return None  

    try:
        cursor.execute("SELECT id_Mail, id_Type FROM  Compte")
        cursor = conn.cursor(mysql.cursors.DictCursor)
        users = cursor.fetchall()
        return users
    
    except mysql.connector.Error as err:
        print(f"Erreur lors de la récupération : {err}")
        return None

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

        user = Recupération_des_utilisateurs(email)  # Récupère l'utilisateur en BDD

        if user and bcrypt.check_password_hash(user['id_Mdp'], password):  # Vérifie le mot de passe
            session['user_id'] = user['id_Utilisateur']
            session['email'] = user['id_Mail']
            session['role'] = user['id_Type']
            flash(f"Bienvenue, {user['id_Mail']} !", 'success')
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
        return redirect(url_for('Creation_compte')) #Erreur si tous els champs ne sont pas compéltés

    nom = data["Nom"]
    prenom = data.get("Prenom", "")  # Optionnel
    societe = data.get("Sociétée", "")  # Optionnel
    mail = data["Mail"]
    mot_de_passe = data["Mdp"]
    mot_de_passe_confirmation = data["Mdp_2"]
    num = data["Num"]

    if mot_de_passe != mot_de_passe_confirmation:
            flash("Les mots de passe ne correspondent pas.", 'danger')
            return redirect(url_for('Creation_compte'))


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
        Envoie_mail_confirmation(mail)
        return redirect(url_for('Creation_compte'))

    except mysql.connector.Error as e:
        conn.rollback()
        flash(f"Erreur lors de la création du compte : {str(e)}", 'danger')
        return redirect(url_for('Creation_compte'))