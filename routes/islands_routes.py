from flask import Flask, Blueprint,jsonify
from Model.Island import Island

islands_routes = Blueprint("islands_routes",__name__)

# Islands routes

@islands_routes.route("/islands",methods=['GET'])
def showAllIslands():
    islands = Island.allIslands()
    return jsonify(islands)

@islands_routes.route("/island/<int:id>", methods=['GET'])
def showIslandById(id):
    island = Island.islandById(id=id)
    return jsonify(island)
