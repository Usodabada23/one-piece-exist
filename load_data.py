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

                cursor.execute("SELECT id FROM devilfruits WHERE name = %s;", (fruit['name'],))
                existing_fruit = cursor.fetchone()

                if existing_fruit:
                    continue

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

def insert_pirates():
    db = Database()
    conn = db.getConnection()
    if conn:
        try:
            cursor = conn.cursor()
            pirates = load_json('pirates.json')
            for pirate in pirates:
                
                cursor.execute("SELECT id FROM pirates WHERE name = %s;", (pirate['name'],))
                existing_pirate = cursor.fetchone()

                if existing_pirate:
                    print(f"✅ Pirate '{pirate['name']}' already exists. Skipping...")
                    continue

                
                cursor.execute("""
                    INSERT INTO pirates (name, age, height, birthDate, bounty, weapon, devilFruit_id, was_supernova)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    pirate['name'],
                    pirate['age'],
                    pirate['height'],
                    pirate['birthDate'],
                    pirate['bounty'],
                    pirate['weapon'],
                    pirate['devilFruit_id'],
                    pirate['was_supernova']
                ))
            conn.commit()
            print("✅ Pirates have been successfully inserted!")
        except Exception as e:
            print(f"❌ An error occurred while inserting the pirates: {e}")
        finally:
            cursor.close()
            db.closeConnection()

def insert_marines():
    db = Database()
    conn = db.getConnection()
    if conn:
        try:
            cursor = conn.cursor()
            marines = load_json('marines.json')
            for marine in marines:
                
                cursor.execute("SELECT id FROM marines WHERE name = %s;", (marine['name'],))
                existing_marine = cursor.fetchone()

                if existing_marine:
                    print(f"✅ Marine '{marine['name']}' already exists. Skipping...")
                    continue

                
                cursor.execute("""
                    INSERT INTO marines (name, age, height, cgbounty, weapon, devilFruit_id, rank)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    marine['name'],
                    marine['age'],
                    marine['height'],
                    marine['cgbounty'],
                    marine['weapon'],
                    marine['devilFruit_id'],
                    marine['rank']
                ))
            conn.commit()
            print("✅ Marines have been successfully inserted!")
        except Exception as e:
            print(f"❌ An error occurred while inserting the marines: {e}")
        finally:
            cursor.close()
            db.closeConnection()

def insert_godsknights():
    db = Database()
    conn = db.getConnection()
    if conn:
        try:
            cursor = conn.cursor()
            godsknights = load_json('godsknights.json')
            for knight in godsknights:
                
                cursor.execute("SELECT id FROM godsknights WHERE name = %s;", (knight['name'],))
                existing_knight = cursor.fetchone()

                if existing_knight:
                    continue

                
                cursor.execute("""
                    INSERT INTO godsknights (name, godFamily, weapon, devilFruit_id)
                    VALUES (%s, %s, %s, %s)
                """, (
                    knight['name'],
                    knight['godFamily'],
                    knight['weapon'],
                    knight['devilFruit_id']
                ))
            conn.commit()
            print("✅ Gods Knights have been successfully inserted!")
        except Exception as e:
            print(f"❌ An error occurred while inserting the gods knights: {e}")
        finally:
            cursor.close()
            db.closeConnection()


insert_devilFruits()