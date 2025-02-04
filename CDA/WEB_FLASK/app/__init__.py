from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'SECRET_KEY'


from app import routes
import os
app.config['SECRET_KEY'] = os.urandom(24)