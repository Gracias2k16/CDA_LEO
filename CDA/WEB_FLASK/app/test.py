import smtplib

email = 'pb.importation@gmail.com'
password = 'PB.Import'

try:
    # Créez une connexion au serveur SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Démarre la connexion sécurisée
    server.login(email, password)  # Authentifiez-vous
    print("Connexion réussie")
except Exception as e:
    print(f"Erreur de connexion : {e}")
finally:
    try:
        server.quit()  # Fermez la connexion si elle a été établie
    except NameError:
        print("La connexion au serveur n'a pas pu être établie, donc 'server' n'est pas défini.")