#!/bin/bash

# IMPORTANT : Modifiez ces variables avec vos informations
DOMAIN="pbimportation.duckdns.org"  # Remplacez par votre domaine DuckDNS
EMAIL="pb.importation@gmail.com"     # Remplacez par votre email

# Vérifier si le script est exécuté en tant que root
if [ "$EUID" -ne 0 ]
  then echo "Ce script doit être exécuté en tant que root ou avec sudo"
  exit
fi

echo "=== Préparation pour l'obtention des certificats SSL ==="

# Mettre à jour la configuration Nginx avec le bon domaine
sed -i "s/pbimportation.duckdns.org/$DOMAIN/g" nginx/conf/app.conf

# Redémarrer Nginx pour appliquer la configuration
echo "Redémarrage de Nginx avec la nouvelle configuration..."
docker compose restart nginx

# Vérifier si Nginx a démarré correctement
sleep 2
if ! docker ps | grep -q nginx-web; then
  echo "ERREUR : Nginx n'a pas démarré correctement."
  docker compose logs nginx
  exit 1
fi

echo "=== Obtention des certificats SSL avec Let's Encrypt ==="
echo "Domaine : $DOMAIN"
echo "Email : $EMAIL"

# Exécuter Certbot pour obtenir les certificats
docker compose run --rm certbot certonly --webroot \
  --webroot-path=/var/www/certbot \
  --email $EMAIL \
  --agree-tos \
  --no-eff-email \
  -d $DOMAIN

# Vérifier si l'obtention du certificat a réussi
if [ $? -ne 0 ]; then
  echo "ERREUR : L'obtention du certificat a échoué."
  exit 1
fi

echo "=== Activation de la configuration HTTPS ==="

# Activer la redirection HTTP vers HTTPS
sed -i 's/# return 301/return 301/g' nginx/conf/default.conf

# Activer le bloc serveur HTTPS
sed -i 's/# server {/server {/g' nginx/conf/default.conf
sed -i 's/#     listen/    listen/g' nginx/conf/default.conf
sed -i 's/#     server_name/    server_name/g' nginx/conf/default.conf
sed -i 's/#     ssl_certificate/    ssl_certificate/g' nginx/conf/default.conf
sed -i 's/#     ssl_certificate_key/    ssl_certificate_key/g' nginx/conf/default.conf
sed -i 's/#     ssl_protocols/    ssl_protocols/g' nginx/conf/default.conf
sed -i 's/#     ssl_prefer_server_ciphers/    ssl_prefer_server_ciphers/g' nginx/conf/default.conf
sed -i 's/#     location/    location/g' nginx/conf/default.conf
sed -i 's/#         root/        root/g' nginx/conf/default.conf
sed -i 's/#         index/        index/g' nginx/conf/default.conf
sed -i 's/# }/}/g' nginx/conf/default.conf

# Mettre à jour les chemins des certificats avec le bon domaine
sed -i "s/votre-domaine.duckdns.org/$DOMAIN/g" nginx/conf/default.conf

# Redémarrer Nginx pour appliquer la configuration SSL
echo "Redémarrage de Nginx avec la configuration SSL..."
docker-compose restart nginx

echo "=== Configuration SSL terminée ==="
echo "Votre site devrait maintenant être accessible en HTTPS : https://$DOMAIN"
echo "Pour vérifier la configuration, utilisez : docker-compose logs nginx"