import mysql.connector
from utils.connection_db import ConnectionDB
from models.langue import Langue
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("MySQL.DB.HOST")
USER = os.getenv("MySQL.DB.USER")
PASSWORD = os.getenv("MySQL.DB.PASSWORD")
NAME = os.getenv("MySQL.DB.NAME")

if __name__ == "__main__":

    connexionDB = ConnectionDB(HOST, USER, PASSWORD, NAME)
    connexion = connexionDB.connecter()


    lang = Langue("Français", "fr-ca")
    lang.ajouter(connexion)
    langues = lang.get_all(connexion=connexion)
    connexion.close()

    for langue in langues:
        langue.affichage()
