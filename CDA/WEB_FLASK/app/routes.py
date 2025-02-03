from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector
import bcrypt
from app import app
from app.forms import ConfigForm

#===================================================================================================

@app.route('/Connexion', methods=['GET', 'POST'])
def login_form():
    return render_template('Connexion.html')


#===================================================================================================

@app.route('/')
def home():
    return render_template('home.html')

#===================================================================================================

@app.route('/Demande')
def Demande():
    return render_template('Demande.html')
