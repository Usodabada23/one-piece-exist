from flask import Flask, Blueprint,jsonify
from Model.Marine import Marine

marines_routes = Blueprint("marines_routes",__name__)

# Marines routes
@marines_routes.route("/marines",methods=['GET'])
def showAllMarines():
    marines = Marine.allMarines()
    return jsonify(marines)

@marines_routes.route("/marine/<int:id>", methods=['GET'])
def showMarineById(id):
    marine = Marine.marineById(id=id)
    return jsonify(marine)

