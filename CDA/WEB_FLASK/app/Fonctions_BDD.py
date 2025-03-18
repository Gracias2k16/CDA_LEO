import mysql.connector
from app.Setting import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_USERNAME, Email_MDP, Email
import smtplib
from email.message import EmailMessage

#===================================================================================================

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

def Deconnexion():
    conn, cur = connexion_à_BDD()
    if cur:
        cur.close()
    if conn and conn.is_connected():
        conn.close()
        print(" Déconnexion OK")

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
    finally:
        cur.close()
        conn.close()