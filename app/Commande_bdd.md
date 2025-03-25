### Méthodes du Curseur
1. **`execute(query, params=None)`** : Cette méthode exécute une requête SQL. Elle peut inclure des paramètres pour protéger contre les injections SQL. Par exemple, `cursor.execute("SELECT * FROM utilisateurs WHERE age > %s", (30,))` exécute une requête pour récupérer tous les utilisateurs de plus de 30 ans.

2. **`executemany(query, param_list)`** : Exécute la même requête SQL plusieurs fois avec différents paramètres. Par exemple, `cursor.executemany("INSERT INTO utilisateurs (nom, age) VALUES (%s, %s)", [('Alice', 30), ('Bob', 25)])` insère plusieurs utilisateurs dans la table.

3. **`fetchall()`** : Récupère toutes les lignes du résultat d'une requête. Par exemple, après `cursor.execute("SELECT * FROM utilisateurs")`, la méthode `resultats = cursor.fetchall()` renverra toutes les lignes correspondantes.

4. **`fetchone()`** : Récupère une seule ligne du résultat d'une requête. Par exemple, `ligne = cursor.fetchone()` retournera la première ligne du résultat.

5. **`fetchmany(size)`** : Récupère un nombre spécifique de lignes. Par exemple, `lignes = cursor.fetchmany(5)` récupère les 5 premières lignes du résultat.

6. **`callproc(procname, params=None)`** : Appelle une procédure stockée dans la base de données. Par exemple, `cursor.callproc('ma_procedure', [param1, param2])` appelle la procédure `ma_procedure` avec les paramètres spécifiés.

7. **`close()`** : Ferme le curseur pour libérer les ressources. Par exemple, `cursor.close()` ferme le curseur après utilisation.

### Méthodes de la Connexion
1. **`commit()`** : Enregistre (ou "commit") les modifications faites à la base de données, comme des insertions ou des mises à jour. Par exemple, `connexion.commit()` permet de sauvegarder les modifications effectuées.

2. **`rollback()`** : Annule les modifications non enregistrées. Par exemple, `connexion.rollback()` annule toutes les modifications depuis le dernier `commit()`.

3. **`close()`** : Ferme la connexion à la base de données. Par exemple, `connexion.close()` termine la connexion.

4. **`cursor()`** : Crée un nouvel objet curseur pour exécuter des requêtes SQL. Par exemple, `cursor = connexion.cursor()` crée un curseur à partir de la connexion.

### Principales Commandes SQL en Python
1. **`SELECT`** : Récupère des données d'une table. Par exemple, `cursor.execute("SELECT * FROM utilisateurs")` récupère toutes les lignes de la table `utilisateurs`.

2. **`INSERT`** : Insère de nouvelles données dans une table. Par exemple, `cursor.execute("INSERT INTO utilisateurs (nom, age) VALUES (%s, %s)", ('Alice', 30))` insère un nouvel utilisateur nommé Alice.

3. **`UPDATE`** : Modifie des données existantes. Par exemple, `cursor.execute("UPDATE utilisateurs SET age = %s WHERE nom = %s", (35, 'Alice'))` met à jour l'âge de l'utilisateur Alice.

4. **`DELETE`** : Supprime des données d'une table. Par exemple, `cursor.execute("DELETE FROM utilisateurs WHERE nom = %s", ('Alice',))` supprime l'utilisateur Alice de la table.

### Autres Méthodes Utiles
1. **`rowcount`** : Cette propriété indique le nombre de lignes affectées par la dernière requête exécutée. Par exemple, `print(cursor.rowcount)` affiche le nombre de lignes modifiées ou retournées.

2. **`description`** : Renvoie une description des colonnes du résultat d'une requête. Par exemple, `print(cursor.description)` affiche des informations sur les colonnes, comme leur nom et leur type.
