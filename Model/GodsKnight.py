from Model.Database import Database
class GodsKnight: 
    def __init__(self,name:str,godFamily:str,weapon:str,devilFruit_id:int):
        self.__name = name
        self.__godFamily = godFamily
        self.__weapon = weapon
        self.__devilFruit_id=devilFruit_id
    
    @staticmethod
    def allGodsKnights():
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM godsknights;"
                cursor.execute(query)
                marines = cursor.fetchall()
                return marines
            except Exception as e:
                print(f"❌ Error fetching gods knights info : {e}")
                return None
    @staticmethod
    def godknightById(id:int):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """SELECT * FROM godsknights WHERE id = %s;"""
                cursor.execute(query,(id,))
                marine = cursor.fetchone()
                return marine
            except Exception as e:
                print(f"❌ Error to fetch god knight with id : {id} : {e}")
                return None