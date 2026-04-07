class Langue:
    def __init__(self, db_connection):
        self.db = db_connection
        self.curseur = self.db.cursor()
    
    def ajouter(self, id, nom, code):
        sql = "INSERT INTO langue (id, nom, code_pays) VALUES (%s, %s, %s)"
        valeurs = (id, nom, code)
        self.curseur.execute(sql, valeurs)
        self.db.commit()
        
    def affichage(self):
        sql = "SELECT * FROM langue"
        self.curseur.execute(sql)
        
        resultats = self.curseur.fetchall()
        return resultats
    