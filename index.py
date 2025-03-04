from flask import Flask
from Model.Database import Database
from Model.Pirate import Pirate
from flask import jsonify
app = Flask(__name__)
@app.route("/")
def hello_world():
    db = Database()
    db.create_tables()  
    return "Hello, World! The One piece exist!"

@app.route("/pirates",methods=['GET'])
def showAllPirates():
    pirates = Pirate.allPirates()
    return jsonify(pirates)

@app.route("/pirate/<int:id>", methods=['GET'])
def showPirateById(id):
    pirate = Pirate.pirateById(id=id)
    return jsonify(pirate)


if __name__ == "__main__":
    app.run(debug=True)
