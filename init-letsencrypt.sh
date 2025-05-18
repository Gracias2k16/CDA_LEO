#!/bin/bash

# Script pour initialiser les certificats Let's Encrypt avec Certbot

if ! [ -x "$(command -v docker)" ]; then
  echo 'Erreur: Docker n'est pas installé.' >&2
  exit 1
fi

if ! [ -x "$(command -v docker-compose)" ]; then
  echo 'Erreur: Docker Compose n'est pas installé.' >&2
  exit 1
fi

domains=(pbimportation.duckdns.org) # Remplacez par votre nom de domaine DuckDNS
rsa_key_size=4096
data_path="./certbot"
email="pb.importation@gmail.com" # Remplacez avec votre email pour les notifications Let's Encrypt
staging=0 # Mettre à 1 pour tester le processus sans limite de rate

if [ -d "$data_path" ]; then
  read -p "Certificats existants trouvés. Continuer et écraser? (y/N) " decision
  if [ "$decision" != "Y" ] && [ "$decision" != "y" ]; then
    exit
  fi
fi

if [ ! -d "$data_path/conf" ]; then
  mkdir -p "$data_path/conf"
fi
if [ ! -d "$data_path/www" ]; then
  mkdir -p "$data_path/www"
fi

echo "### Création de configuration nginx temporaire ..."
mkdir -p "./nginx/conf"
cat > "./nginx/conf/app.conf" << 'EOF'
server {
    listen 80;
    server_name pbimportation.duckdns.org;  # Remplacez par votre nom de domaine DuckDNS
    
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }
    
    location / {
        return 301 https://$host$request_uri;
    }
}
EOF

sed -i "s/pbimportation.duckdns.org/${domains[0]}/g" "./nginx/conf/app.conf"
mkdir -p "./nginx/html"

echo "### Démarrage de nginx ..."
docker-compose up --force-recreate -d nginx
echo

echo "### Obtention des certificats SSL ..."
path="/etc/letsencrypt/live/$domains"

# Sélectionner les paramètres appropriés selon staging ou production
domain_args=""
for domain in "${domains[@]}"; do
  domain_args="$domain_args -d $domain"
done

email_arg="--email $email"
if [ $staging != "0" ]; then
  staging_arg="--staging"
fi

docker-compose run --rm --entrypoint "\
  certbot certonly --webroot -w /var/www/certbot \
    $staging_arg \
    $email_arg \
    $domain_args \
    --rsa-key-size $rsa_key_size \
    --agree-tos \
    --force-renewal" certbot
echo

echo "### Rechargement nginx ..."
docker-compose exec nginx nginx -s reload

echo "### Configuration terminée!"
echo "### Veuillez maintenant créer votre fichier de configuration nginx définitif"
echo "### et relancer docker-compose avec 'docker-compose up -d'"