from flask import Flask
from Model.Database import Database
from Model.Pirate import Pirate
from Model.Marine import Marine
from flask import jsonify
app = Flask(__name__)
@app.route("/")
def hello_world():
    db = Database()
    db.create_tables()  
    return "Hello, World! The One piece exist!"

# Pirates routes
@app.route("/pirates",methods=['GET'])
def showAllPirates():
    pirates = Pirate.allPirates()
    return jsonify(pirates)

@app.route("/pirate/<int:id>", methods=['GET'])
def showPirateById(id):
    pirate = Pirate.pirateById(id=id)
    return jsonify(pirate)

# Marines routes

@app.route("/marines",methods=['GET'])
def showAllMarines():
    marines = Marine.allMarines()
    return jsonify(marines)

@app.route("/marine/<int:id>", methods=['GET'])
def showMarineById(id):
    marine = Marine.marineById(id=id)
    return jsonify(marine)

if __name__ == "__main__":
    app.run(debug=True)
