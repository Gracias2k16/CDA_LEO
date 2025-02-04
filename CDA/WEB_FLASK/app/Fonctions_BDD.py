import mysql.connector
from app.Setting import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_USERNAME

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

def Recupération_de_comptes():
    conn, cur = connexion_à_BDD()
    if conn is None or cur is None:
        return
    
    try:
        cur.execute("SELECT * FROM Compte") 
        resultats = cur.fetchall()

        for ligne in resultats:
            print(ligne)  
    except mysql.connector.Error as err:
        print(f" Erreur lors de la récupération : {err}")


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

Ecriture_adresse()
