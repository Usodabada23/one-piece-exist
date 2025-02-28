from DevilFruit import DevilFruit 
from Database import Database

class Pirate:
    def __init__(self,name:str,age:int,height:int,birthDate:str,bounty:int,weapon:str,devilFruit_id:int,was_supernova:bool):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__birthDate = birthDate
        self.__bounty = bounty
        self.__weapon = weapon
        self.__devilFruit_id = devilFruit_id
        self.__was_supernova = was_supernova

    """
    def add(self):
        db = Database()
        conn = db.getConnection()
        if conn:
            cursor = conn.cursor()

    """

    @staticmethod
    def allPirates():
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM pirates;"
                cursor.execute(query)
                pirates = cursor.fetchall()
                return pirates
            except Exception as e:
                print(f"❌ Erreur lors de la récupération des pirates : {e}")
                return []