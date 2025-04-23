1. Sur le Raspberry Pi :
a) Installer Docker
Si Docker n'est pas encore installé, voici les commandes à utiliser sur le Raspberry Pi :

Konsole :

# Mettre à jour les paquets
sudo apt-get update

# Installer les dépendances nécessaires pour Docker
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

# Ajouter la clé GPG de Docker
curl -fsSL https://download.docker.com/linux/raspbian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Ajouter le dépôt Docker
echo "deb [arch=armhf signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/raspbian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Mettre à jour les paquets et installer Docker
sudo apt-get update
sudo apt-get install docker-ce

# Installer Docker Compose
sudo apt-get install -y python3-pip
sudo pip3 install docker-compose


2. Préparer ton projet sur le Raspberry Pi
a) Copier ton code sur le Raspberry Pi
Tu peux transférer tout ton projet vers ton Raspberry Pi en utilisant scp (ou même Git si tu l'as configuré sur le Pi) :

Konsole :

# Copier tout le projet dans un dossier sur le Raspberry Pi
scp -r /chemin/vers/ton/projet pi@<ip_du_raspberry>:/home/pi/ton_dossier

3. Lancer tes conteneurs Docker :
a) Dans le dossier de ton projet sur le Raspberry Pi, lance les conteneurs Docker avec :

Konsole :

docker-compose up --build
Cela va construire ton image Docker, lancer tes services (Flask, Adminer, MySQL) et te préparer à démarrer l'app.

4. Exécuter le script run.sh :
a) Pour lancer ton app Flask, tu n’as plus qu'à exécuter le script run.sh que tu as préparé :

Konsole :

./run.sh



Résumé du processus sur le Raspberry Pi :
Installer Docker et Docker Compose (si pas déjà fait)

Transférer ton code sur le Raspberry Pi

Lancer Docker Compose avec docker-compose up --build

Lancer l’app avec ./run.sh