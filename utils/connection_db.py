import mysql.connector
from mysql.connector import Error


class ConnectionDB :
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "Tin@97k@nto2001"
        self.database = "foodly"
        self.connection = None
    def connecter(self) :
        """Établit la connexion à la base de données."""
        try: 
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("✅ Connexion à 'foodly' réussie !")
                return self.connection
        except Error as e:
            print(f"❌ Erreur lors de la connexion : {e}")
            return None
    def deconnecter(self):
        """Ferme la connexion."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connection fermée")