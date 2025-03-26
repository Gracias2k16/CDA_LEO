import os
from dotenv  import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

#//////////////////////////////  Gestion BDD   ////////////////////////////

DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")

#//////////////////////////////  Gestion Email   ////////////////////////////

Email_MDP = os.getenv ("Adressemail_MDP")
Email = os.getenv ("Adressemail")