ADMINER 
root
uimm

BDD:
Insert
create
update
delete

INSERT INTO Adresse
(id_N_Rue, id_CP, id_Cmplt_rue, id_Ville, id_Nom_rue)
VALUES (37, 35470, '','Bain-de-bretagne', 'Rue des résistants');


Commande insertion python dans bdd:
sql = "IINSERT INTO Adresse
(id_N_Rue, id_CP, id_Cmplt_rue, id_Ville, id_Nom_rue)
VALUES (37, 35470, '','Bain-de-bretagne', 'Rue des résistants');


cur.execute(sql, Values)
conn.commit()

print(f"{cur.rowcount} enregistrement inséré.")

Afficher une table :
cur.execute("SELECT * FROM utilisateurs")
resultats = cur.fetchall()

for ligne in resultats:
    print(ligne)

Afficher une ligne :

cur.execute("SELECT * FROM utilisateurs LIMIT 1")
ligne = cur.fetchone()
print(ligne)

Afficher une donée filtrée:

cur.execute("SELECT * FROM utilisateurs WHERE age > 25")
resultats = cur.fetchall()

for ligne in resultats:
    print(ligne)