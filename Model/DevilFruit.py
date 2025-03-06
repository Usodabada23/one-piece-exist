from Model.TypeDevilFruit import TypeDevilFruit
from Model.Database import Database
class DevilFruit:
    def __init__(self,name: str,typeFruit: TypeDevilFruit,description: str,ability: str,rarity: str,isEaten: bool):
        self.__name = name
        self.__typeFruit = typeFruit
        self.__description = description
        self.__ability = ability
        self.__rarity = rarity
        self.__isEaten = isEaten

    def add(self):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """INSERT INTO devilfruits (name,typeFruit,description,ability,rarity,is_eaten) VALUES
                    (%s,%s,%s,%s,%s,%s) ;"""
                cursor.execute(query, (
                    self.__name,
                    self.__typeFruit,
                    self.__description,
                    self.__ability,
                    self.__rarity,
                    self.__isEaten,
                ))
                conn.commit()  # Save changes
                print("✅ devil fruit added to db!")
            except Exception as e:
                print(f"❌ Error insert devil fruit {self.__name} : {e}")
                return None

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
    @staticmethod
    def delete(id:int):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """DELETE FROM devilfruits WHERE id = %s;"""
                cursor.execute(query,(id,))
                conn.commit()
                success = cursor.rowcount > 0
                cursor.close()
                conn.close()
                return success
            except Exception as e:
                print(f"❌ Error to delete devil Fruit with id : {id} : {e}")
                return None


    