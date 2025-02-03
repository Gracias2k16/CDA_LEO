import mysql.connector


#===================================================================================================

def conncexion_à_BDD():
    try:
        conn = mysql.connector.connect(# Connexion à la base de données
        host="localhost",
        user="root",
        password="uimm",
        database="CDA_Léo_import"
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
    conn, cur = conncexion_à_BDD()
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

def Deconnexion(conn, cur):
    if cur:
        cur.close()
    if conn and conn.is_connected():
        conn.close()
        print(" Déconnexion OK")

#===================================================================================================
conncexion_à_BDD()

