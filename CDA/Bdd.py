import mysql.connector


#===================================================================================================

#===================================================================================================


def Connection (pwd) :

    global connexion
    password = pwd

    config = {
        'user': 'root',
        'password': password,
        'host': 'localhost',
        'database': 'CDA'
    }

    try:
        connexion = mysql.connector.connect(**config)# Connexion à la base de données
        print(f'Connection réussie')

    except : #Détection d'erreurs
        print(f"Erreur lors de la connection")


#===================================================================================================


def Identifiants():

    try :
        
        mycursor = connexion.cursor()# Création d'un curseur
             
        mycursor.execute("SELECT Identifiant , Mot_de_passe FROM Utilisateurs") # Requette

        for x in mycursor : # Ecriture des infos sur chaque lignes
            print(x)
        print ("================")

    except : #Détection d'erreurs
        print(f"Erreur lors de la récupérationd le données")


#===================================================================================================


def Deconnection():

    try :
        
        if connexion:  # Controle si la connexion est créée avant de la fermer
            connexion.close()
        print(f'Déconnection réussie')

    except : #Détection d'erreurs
        print(f"Erreur lors de la déconnection")


#===================================================================================================

if __name__ == '__main__':

    pwd = input("Entrez le mot de passe de la  BDD :")
    
    try :
        Connection(pwd)
        Identifiants()
        Deconnection()

    except :
        print(f'erreur')


    

