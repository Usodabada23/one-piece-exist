from flask import Flask
from Model.Database import Database

app = Flask(__name__)
@app.route("/")
def hello_world():
    db = Database()
    db.create_tables()  
    return "Hello, World! The One piece exist!"

if __name__ == "__main__":
    app.run(debug=True)
