from flask import Flask, Blueprint,jsonify
from Model.GodsKnight import GodsKnight

godsKnights_routes = Blueprint("godsKnights_routes",__name__)

# Gods Knights routes

@godsKnights_routes.route("/godsKnights",methods=['GET'])
def showAllGodsKnights():
    godsknights = GodsKnight.allGodsKnights()
    return jsonify(godsknights)

@godsKnights_routes.route("/godKnight/<int:id>", methods=['GET'])
def showGodknightById(id):
    godknight = GodsKnight.godknightById(id=id)
    return jsonify(godknight)
