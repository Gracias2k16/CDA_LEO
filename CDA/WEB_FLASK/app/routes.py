from flask import request, render_template, flash, redirect, url_for, session
import mysql.connector
from app import app
from app.Fonctions_BDD import connexion_à_BDD, Recupération_des_utilisateurs, Envoie_mail_confirmation
from app.__init__ import bcrypt
import mysql
from flask import jsonify


#===================================================================================================

@app.route('/Connexion', methods=["GET", "POST"])
def Connexion():
    if request.method == 'POST':
        email = request.form['identifiant']
        password = request.form['password']

        user = Recupération_des_utilisateurs(email)  # Récupère l'utilisateur en BDD

        if user and bcrypt.check_password_hash(user['id_Mdp'], password):  # Vérifie le mot de passe
            session['user_id'] = user['id_Utilisateur']
            session['email'] = user['id_Mail']
            session['role'] = user['id_Type']
            flash(f"Bienvenue, {user['id_Mail']} !", 'success')
            return redirect(url_for('home'))
        else:
            flash("Identifiant ou mot de passe incorrect.", 'danger')

    return render_template ('Connexion.html')

#===================================================================================================

@app.route('/')
def home():
    return render_template('home.html')

#===================================================================================================

@app.route('/Demande')
def Demande():
    return render_template('Demande.html')

#===================================================================================================

@app.route('/Creation_compte', methods=['GET', 'POST'])
def Creation_compte():
    if request.method == 'GET':
        return render_template('Creation_compte.html')  # Affiche la page HTML avec le formulaire

    elif request.method == 'POST':
        data = request.form  # Récupère les données envoyées par le formulaire

    required_fields = ["Nom", "Mail","Mdp", "Mdp_2","Num"] # Champs requis
    if not all(field in data and data[field] for field in required_fields):
        flash("Certains champs obligatoires sont manquants.", 'danger')
        return redirect(url_for('Creation_compte')) #Erreur si tous els champs ne sont pas compéltés

    nom = data["Nom"]
    prenom = data.get("Prenom", "")  # Optionnel
    societe = data.get("Sociétée", "")  # Optionnel
    mail = data["Mail"]
    mot_de_passe = data["Mdp"]
    mot_de_passe_confirmation = data["Mdp_2"]
    num = data["Num"]

    if mot_de_passe != mot_de_passe_confirmation:
            flash("Les mots de passe ne correspondent pas.", 'danger')
            return redirect(url_for('Creation_compte'))


    hashed_password = bcrypt.generate_password_hash(mot_de_passe).decode('utf-8')

    conn, cur = connexion_à_BDD()  # Connexion à la BDD
    if conn is None or cur is None:
        flash("Impossible de se connecter à la base de données.", 'danger')
        return redirect(url_for('Creation_compte'))
    
    try:
        cur.execute("SELECT * FROM Compte WHERE id_Mail = %s", (mail,))# Vérifier si l'email existe déjà
        if cur.fetchone():
            flash("Cet email est déjà utilisé.", 'danger')
            return redirect(url_for('Creation_compte'))

        sql = "INSERT INTO Compte (id_Nom, id_Prenom, id_Nom_societee, id_Mail, id_Mdp, Num_tel, id_Type) VALUES (%s, %s, %s, %s, %s, %s, %s)" #requete sql pour inseré le compte
        cur.execute(sql, (nom, prenom, societe, mail, hashed_password, num, 'USER'))
        conn.commit()

        flash("Compte créé avec succès !", 'success')
        Envoie_mail_confirmation(mail)
        return redirect(url_for('Creation_compte'))

    except mysql.connector.Error as e:
        conn.rollback()
        flash(f"Erreur lors de la création du compte : {str(e)}", 'danger')
        return redirect(url_for('Creation_compte'))

    finally:
        cur.close()
        conn.close()

#===================================================================================================

@app.route('/session-data')
def session_data():
    return jsonify(dict(session))

#===================================================================================================

@app.route('/logout')
def logout():
    session.clear()
    flash("Déconnexion réussie.", "success")
    return redirect(url_for('Connexion'))

#===================================================================================================

@app.route('/Comptes')
def Comptes():
    conn, cur = connexion_à_BDD() 
    if conn is None or cur is None:
        return render_template('Comptes.html', users=[])

    try:
        cur.execute("SELECT id_Mail, id_Type FROM  Compte")
        users = cur.fetchall()
        #print(f"Récupération OK")
        print(users)
        return render_template('Comptes.html', users=users)
    
    except mysql.connector.Error as err:
        print(f"Erreur lors de la récupération : {err}")
        return render_template('Comptes.html', users=[])
    
    finally:
        cur.close()
        conn.close()

#===================================================================================================

@app.route('/supprimer_selection', methods=['POST'])
def supprimer_selection():
    selected_users = request.form.getlist('selected_users')
    print(f"Utilisateurs sélectionnés : {selected_users}")

    if selected_users:
        conn, cur = connexion_à_BDD()

        try:
            format_strings = ','.join(['%s'] * len(selected_users))  # Création des placeholders SQL
            query = f"DELETE FROM Compte WHERE id_Mail IN ({format_strings})"
            cur.execute(query, tuple(selected_users))
            conn.commit()
            flash("Utilisateurs supprimés avec succès.", "success")
        except mysql.connector.Error as err:
            print(f"Erreur : {err}")
            flash("Erreur lors de la suppression.", "danger")
        finally:
            cur.close()
            conn.close()
    
    return redirect(url_for('Comptes'))

#===================================================================================================

@app.route('/modifier_role', methods=['POST'])
def modifier_role():
    conn, cur = connexion_à_BDD()

    try:
        for user in request.form:
            if user.startswith('new_role_'):
                user_email = user.split('_', 2)[-1]
                new_role = request.form[user]
                print(f"Modification de {user_email} au rôle {new_role}")

            cur.execute("UPDATE Compte SET id_Type = %s WHERE id_Mail = %s", (new_role, user_email))
            conn.commit()

        flash("Les rôles ont été modifiés avec succès.", "success")

    except mysql.connector.Error as err:
        print(f"Erreur lors de la modification des rôles : {err}")
        flash("Erreur lors de la modification des rôles.", "danger")
    finally:
        cur.close()
        conn.close()

    return redirect(url_for('Comptes'))