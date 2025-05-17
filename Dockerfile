FROM python:3.13-slim

WORKDIR /app

# Copie du code
COPY app/ .

# Install des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port Flask
EXPOSE 5000

# Lance l’app Flask
COPY run.sh /run.sh

RUN chmod +x /run.sh
CMD ["sh", "run.sh"]
