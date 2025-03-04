from flask import Flask
from Model.Database import Database
from Model.Pirate import Pirate
from Model.Marine import Marine
from Model.Island import Island
from Model.GodsKnight import GodsKnight
from Model.DevilFruit import DevilFruit
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

# Islands routes

@app.route("/islands",methods=['GET'])
def showAllIslands():
    islands = Island.allIslands()
    return jsonify(islands)

@app.route("/island/<int:id>", methods=['GET'])
def showIslandById(id):
    island = Island.islandById(id=id)
    return jsonify(island)

# Gods Knights routes

@app.route("/godsKnights",methods=['GET'])
def showAllGodsKnights():
    godsknights = GodsKnight.allGodsKnights()
    return jsonify(godsknights)

@app.route("/godKnight/<int:id>", methods=['GET'])
def showGodknightById(id):
    godknight = GodsKnight.godknightById(id=id)
    return jsonify(godknight)

# Devil fruits routes

@app.route("/devilFruits",methods=['GET'])
def showAllDevilFruits():
    devilFruits = DevilFruit.allDevilFruits()
    return jsonify(devilFruits)

@app.route("/devilFruit/<int:id>", methods=['GET'])
def showDevilFruit(id):
    devilFruit = DevilFruit.devilFruitById(id=id)
    return jsonify(devilFruit)


if __name__ == "__main__":
    app.run(debug=True)
