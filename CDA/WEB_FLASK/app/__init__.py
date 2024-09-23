from flask import Flask
app = Flask(__name__)
from app import routes
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)