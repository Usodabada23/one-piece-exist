import psycopg2
from dotenv import load_dotenv
import os
SQL_SCRIPT = """
CREATE TABLE IF NOT EXISTS devilFruits (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    typeFruit VARCHAR(255) NOT NULL,
    description TEXT,
    ability TEXT,
    rarity VARCHAR(50),
    is_eaten BOOLEAN DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS pirates (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    height INT NOT NULL,
    birthDate DATE NOT NULL,
    bounty BIGINT,
    weapon VARCHAR(255),
    devilFruit_id INT NULL,
    was_supernova BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (devilFruit_id) REFERENCES devilFruits(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS godsknights (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    godFamily VARCHAR(255),
    weapon VARCHAR(255),
    devilFruit_id INT NULL,
    FOREIGN KEY (devilFruit_id) REFERENCES devilFruits(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS marines (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    height INT NOT NULL,
    cgbounty VARCHAR(255),
    weapon VARCHAR(255),
    devilFruit_id INT NULL,
    rank VARCHAR(100),
    FOREIGN KEY (devilFruit_id) REFERENCES devilFruits(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS islands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    government VARCHAR(255) NOT NULL,
    affiliated_group VARCHAR(255)
);

"""

class Database:
    
    def __init__(self):
        load_dotenv()
        db_name = os.getenv("DATABASE")  
        host_name= os.getenv("HOST")
        user_name=os.getenv("USER")
        pwd=os.getenv("PASSWORD")
        portnum = os.getenv("PORT")
        try:
            self.conn = psycopg2.connect(database = db_name,
                                    host = host_name,
                                    user = user_name,
                                    password = pwd,
                                    port = portnum)
            
            self.cursor = self.conn.cursor()
            print("database connection success")
        except Exception as e:
            print(f"Error during connection with database : {e}")
            self.conn = None

    def create_tables(self):
        try:
            if self.cursor:
                self.cursor.execute(SQL_SCRIPT)
                self.conn.commit()
                print("✅ Tables créées avec succès !")
        except Exception as e:
            print(f"❌ Erreur lors de la création des tables : {e}")
        finally:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()

    def getConnection(self):
        return self.conn
    
    def closeConnection(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()