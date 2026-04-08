import mysql.connector
from mysql.connector import Error


class ConnectionDB :
    def __init__(self, host, user, password, database) :
        self.host = host
        self.user = user
        self.password = password
        self.database = database


    def connecter(self) :
        """Établit la connexion à la base de données."""
        try: 
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if connection.is_connected():
                print("✅ Connexion à 'script' réussie !")
                return connection
        except Error as e:
            print(f"❌ Erreur lors de la connexion : {e}")
            return None
        