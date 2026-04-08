class Langue:
    def __init__(self, nom, code, id=None):
        self.id = id
        self.nom = nom
        self.code = code

    def ajouter(self, connexion):
        sql = "INSERT INTO langue (nom, code) VALUES (%s, %s)"
        valeurs = (self.nom, self.code)
        curseur = connexion.cursor()
        curseur.execute(sql, valeurs)
        connexion.commit()
        
    def get_all (self, connexion):
        sql = "SELECT * FROM langue"
        curseur = connexion.cursor()
        curseur.execute(sql)
        
        resultats = curseur.fetchall()
        langues = []

        for resultat in resultats:
            langues.append(Langue(resultat[1], resultat[2], id=resultat[0]))
        return langues
    
    def affichage(self):
        print (f"ID: {self.id}, Nom: {self.nom}, Code: {self.code}")