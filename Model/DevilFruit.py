from Model.TypeDevilFruit import TypeDevilFruit
from Model.Database import Database
class DevilFruit:
    def __init__(self,name: str,typeFruit: TypeDevilFruit,description: str,ability: str,rarity: str,is_eaten: bool):
        self.name = name
        self.typeFruit = typeFruit
        self.description = description
        self.ability = ability
        self.rarity = rarity
        self.is_eaten = is_eaten

    @staticmethod
    def allDevilFruits():
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM devilFruits;"
                cursor.execute(query)
                marines = cursor.fetchall()
                return marines
            except Exception as e:
                print(f"❌ Error fetching devil fruits info : {e}")
                return None
    @staticmethod
    def devilFruitById(id:int):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """SELECT * FROM devilFruits WHERE id = %s;"""
                cursor.execute(query,(id,))
                marine = cursor.fetchone()
                return marine
            except Exception as e:
                print(f"❌ Error to fetch devil fruit with id : {id} : {e}")
                return None


    