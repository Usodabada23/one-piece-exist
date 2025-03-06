from Model.Database import Database
class Island:

    def __init__(self, name:str, location:str, government:str, affiliated_group=None):
        """
        Initialise une île avec les informations de base.

        :param name: Nom de l'île (str)
        :param location: Localisation (ex: Grand Line, East Blue, etc.) (str)
        :param government: Type de gouvernement (ex: monarchie, dictature, etc.) (str)
        :param affiliated_group: Groupe ou faction auquel l'île est associée (ex: Marine, Pirates, etc.) (str, optionnel)
        """
        self.__name = name
        self.__location = location
        self.__government = government
        self.__affiliated_group = affiliated_group
    
    def add(self):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """INSERT INTO islands (name,location,government,affiliated_group) VALUES
                    (%s,%s,%s,%s) ;"""
                cursor.execute(query, (
                    self.__name,
                    self.__location,
                    self.__government,
                    self.__affiliated_group,
                ))
                conn.commit()  # Save changes
                print("✅ Island added to db!")
            except Exception as e:
                print(f"❌ Error insert island {self.__name} : {e}")
                return None
            
    @staticmethod
    def allIslands():
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM islands;"
                cursor.execute(query)
                marines = cursor.fetchall()
                return marines
            except Exception as e:
                print(f"❌ Error fetching islands info : {e}")
                return None
    @staticmethod
    def islandById(id:int):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """SELECT * FROM islands WHERE id = %s;"""
                cursor.execute(query,(id,))
                marine = cursor.fetchone()
                return marine
            except Exception as e:
                print(f"❌ Error to fetch island with id : {id} : {e}")
                return None
    
    @staticmethod
    def delete(id:int):
        db = Database()
        conn = db.getConnection()
        if conn:
            try:
                cursor = conn.cursor()
                query = """DELETE FROM islands WHERE id = %s;"""
                cursor.execute(query,(id,))
                conn.commit()
                success = cursor.rowcount > 0
                cursor.close()
                conn.close()
                return success
            except Exception as e:
                print(f"❌ Error to delete island with id : {id} : {e}")
                return None