import smtplib
from Fonctions_BDD import Envoie_mail_confirmation


email = 'pb.importation@gmail.com'
password = 'bogp ffwg dumh tkfc'

try:
    # Utilisation correcte de SMTP_SSL avec le bon port
    server = smtplib.SMTP('smtp.gmail.com', 587)  
    server.starttls()
    server.login(email, password)
    server.sendmail(email, "paimblancleo@orange.fr", "Test email")
    server.quit()
    print("Email envoyé avec succès")
except Exception as e:
    print(f"Erreur : {e}")


#Envoie_mail_confirmation("paimblancleo@orange.fr")