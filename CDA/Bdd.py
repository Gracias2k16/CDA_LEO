import mysql.connector

config = {#Infos concernant la base de donnée
    'user': 'root',
    'password': 'uimm',
    'host': 'localhost',
    'database': 'CDA'
}

try:
    connexion = mysql.connector.connect(**config)# Connexion à la base de données

    mycursor = connexion.cursor()# Création d'un curseur

    mycursor.execute("show databaseS ") # Requette

    for x in mycursor : # Ecriture des infos sur chaque lignes
        print(x)
    print ("================")

except mysql.connector.Error as e: #Détection d'erreurs
    print(f"Erreur : {e}")

finally: # Fermeture du curseur et de la connexion
    mycursor.close()
    connexion.close()