from Model.RankMarine import RankMarine
from Model.Database import Database
class Marine:
    def __init__(self,name:str,age:int,height:int,cgbounty:str,weapon:str,devilFruit_id:int,rank:RankMarine):
        self.__name = name
        self.__age = age
        self.__height = height
        self.__cgbounty = cgbounty
        self.__weapon = weapon
        self.__devilFruit_id= devilFruit_id
        self.__rank = rank
    
    def add(self):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """INSERT INTO marines (name,age,height,cgbounty,weapon,devilFruit_id,rank) VALUES
                    (%s,%s,%s,%s,%s,%s,%s) ;"""
                cursor.execute(query, (
                    self.__name,
                    self.__age,
                    self.__height,
                    self.__cgbounty,
                    self.__weapon,
                    self.__devilFruit_id,
                    self.__rank
                ))
                conn.commit()  # Save changes
                print("✅ Marine added to db!")
            except Exception as e:
                print(f"❌ Error insert marine {self.__name} : {e}")
                return None
            
    @staticmethod
    def allMarines():
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM marines;"
                cursor.execute(query)
                marines = cursor.fetchall()
                return marines
            except Exception as e:
                print(f"❌ Error fetching marines info : {e}")
                return None
    @staticmethod
    def marineById(id:int):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """SELECT * FROM marines WHERE id = %s;"""
                cursor.execute(query,(id,))
                marine = cursor.fetchone()
                return marine
            except Exception as e:
                print(f"❌ Error to fetch marine with id : {id} : {e}")
                return None
    
    @staticmethod
    def delete(id:int):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """DELETE FROM marines WHERE id = %s;"""
                cursor.execute(query,(id,))
                conn.commit()
                success = cursor.rowcount > 0
                cursor.close()
                conn.close()
                return success
            except Exception as e:
                print(f"❌ Error to delete marine with id : {id} : {e}")
                return None


    