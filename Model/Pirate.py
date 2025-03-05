from Model.DevilFruit import DevilFruit 
from Model.Database import Database
import datetime
class Pirate:
    def __init__(self,name:str,age:int,height:int,birthDate:datetime,bounty:int,weapon:str,devilFruit_id,was_supernova:bool):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__birthDate = birthDate
        self.__bounty = bounty
        self.__weapon = weapon
        self.__devilFruit_id = devilFruit_id
        self.__was_supernova = was_supernova

    
    def add(self):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """INSERT INTO pirates (name,age,height,birthDate,bounty,weapon,devilFruit_id,was_supernova) VALUES
                    (%s,%s,%s,%s,%s,%s,%s,%s) ;"""
                cursor.execute(query, (
                    self.__name,
                    self.__age,
                    self.__height,
                    self.__birthDate,
                    self.__bounty,
                    self.__weapon,
                    self.__devilFruit_id,
                    self.__was_supernova
                ))
                conn.commit()  # Save changes
                print("✅ Pirate added !")
            except Exception as e:
                print(f"❌ Erreur lors de la récupération du pirates avec l'id : {id} : {e}")
                return None

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
                return None
    @staticmethod
    def pirateById(id:int):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """SELECT * FROM pirates WHERE id = %s;"""
                cursor.execute(query,(id,))
                pirate = cursor.fetchone()
                return pirate
            except Exception as e:
                print(f"❌ Erreur lors de la récupération du pirates avec l'id : {id} : {e}")
                return None