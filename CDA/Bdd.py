import mysql.connector


#===================================================================================================

#===================================================================================================
class IF_BDD:

    def __init__(sefl, user):
        sefl.connection = None
        sefl.user = user

    def Connection (sefl, pwd) :

        password = pwd

        config = {
            'user': sefl.user,
            'password': password,
            'host': 'localhost',
            'database': 'CDA'
        }

        try:
            sefl.connexion = mysql.connector.connect(**config)# Connexion à la base de données
            print(f'Connection réussie')
            return True

        except : #Détection d'erreurs
            print(f"Erreur lors de la connection")
            return False


    #===================================================================================================


    def Identifiants(sefl):

        try :
        
            mycursor = sefl.connexion.cursor()# Création d'un curseur
             
            mycursor.execute("SELECT Identifiant , Mot_de_passe FROM Utilisateurs") # Requette

            for x in mycursor : # Ecriture des infos sur chaque lignes
                print(x)
            print ("================")

        except : #Détection d'erreurs
            print(f"Erreur lors de la récupérationd le données")


    #===================================================================================================


    def Deconnection(sefl):

        try :
        
            if sefl.connexion:  # Controle si la connexion est créée avant de la fermer
                sefl.connexion.close()
            print(f'Déconnection réussie')

        except : #Détection d'erreurs
            print(f"Erreur lors de la déconnection")


#===================================================================================================

if __name__ == '__main__':

    pwd = input("Entrez le mot de passe de la  BDD :")
    ifbdd = IF_BDD('root')
    
    try :
        ifbdd.Connection(pwd) 
        ifbdd.Identifiants()
        ifbdd.Deconnection()

    except :
        print(f'erreur')


    

