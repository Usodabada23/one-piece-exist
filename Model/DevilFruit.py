import TypeDevilFruit
from Database import Database
class DevilFruit:
    def __init__(self,name: str,typeFruit: TypeDevilFruit,description: str,ability: str,rarity: str,is_eaten: bool):
        self.name = name
        self.typeFruit = typeFruit
        self.description = description
        self.ability = ability
        self.rarity = rarity
        self.is_eaten = is_eaten

    @staticmethod
    def allDevilFruit():
        db = Database()
        conn = db.getConnection()
        try :
            cursor = conn.cursor()
            data = cursor.execute("SELECT * FROM devilfruits;")
            if(data):
                return data
            else:
                return None

        except Exception as e:
            print(f"Error : {e}")
            exit()


    