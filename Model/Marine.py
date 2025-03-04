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


    