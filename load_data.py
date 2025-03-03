from Model.DevilFruit import DevilFruit
from Model.Database import Database
from Model.TypeDevilFruit import TypeDevilFruit
import json

def load_json(file_name):
    with open(f'data/{file_name}','r',encoding="utf-8") as file:
        return json.load(file)

def insert_devilFruits():
    db = Database()
    conn = db.getConnection()
    if conn:
        try:
            cursor = conn.cursor()
            fruits = load_json('devilFruits.json')
            for fruit in fruits:
                cursor.execute("""
                    INSERT INTO devilfruits (name, typefruit, description, ability, rarity, is_eaten)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    fruit['name'],
                    TypeDevilFruit[fruit['type']].value, 
                    fruit['description'],
                    fruit['ability'],
                    fruit['rarity'],
                    fruit['is_eaten']
                ))
            conn.commit()
            print("✅ Devil fruits have been successfully inserted!")
        except Exception as e:
            print(f"❌ An error occurred while inserting the devil fruits: {e}")
        finally:
            cursor.close()
            db.closeConnection()

insert_devilFruits()