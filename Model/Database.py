import psycopg2
from dotenv import load_dotenv
import os
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
        except Exception as e:
            print(f"Error during connection with database : {e}")
            self.conn = None

    def getConnection(self):
        return self.conn
    
    def closeConnection(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()