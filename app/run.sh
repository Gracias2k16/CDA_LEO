#!/bin/bash

cd "$(dirname "$0")"

# Active environnement virtuel
echo "Activation de l'environnement virtuel..."
source ../.venv/bin/activate

# libére le port 5000 si déjà utilisé
PORT=5000
if lsof -i :$PORT >/dev/null; then
  echo "Port $PORT déjà utilisé, on kill le process..."
  kill $(lsof -t -i :$PORT)
fi

echo "Lancement de Flask..."
python ../serverWEB.py