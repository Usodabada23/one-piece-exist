from flask import Flask, Blueprint,jsonify
from Model.Pirate import Pirate

pirates_routes = Blueprint("pirates_routes",__name__)

# Pirates routes
@pirates_routes.route("/pirates",methods=['GET'])
def showAllPirates():
    pirates = Pirate.allPirates()
    return jsonify(pirates)

@pirates_routes.route("/pirate/<int:id>", methods=['GET'])
def showPirateById(id):
    pirate = Pirate.pirateById(id=id)
    return jsonify(pirate)
