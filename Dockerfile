FROM python:3.13-slim

WORKDIR /

# Copie du code
COPY / .

# Install des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port Flask
EXPOSE 5000

# Lance l’app Flask
COPY run.sh .

RUN chmod +x /run.sh
CMD ["sh", "run.sh"]
