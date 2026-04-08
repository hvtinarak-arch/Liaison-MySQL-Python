import mysql.connector
from utils.connection_db import ConnectionDB
from querry.langue import Langue


if __name__ == "__main__":

    ma_base = ConnectionDB()
    db = ma_base.connecter()
    ma_langue = Langue(db)
     
    ma_langue.ajouter("2", "Français", "fr-ca")
    
    ma_langue.affichage()
    langues_enregistrees = ma_langue.affichage()
    print("--- Liste des langues dans la base script ---POUR MODIFICATION be")
    for ligne in langues_enregistrees:
        print(ligne)
    
    
    ma_base.deconnecter()