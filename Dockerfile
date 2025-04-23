FROM python:3.13-slim

WORKDIR /app

# Copie du code
COPY app/ .

# Install des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port Flask
EXPOSE 5000

# Lance l’app Flask
CMD ["python", "main.py"]