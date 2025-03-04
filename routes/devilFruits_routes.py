from flask import Flask, Blueprint,jsonify
from Model.DevilFruit import DevilFruit

devilFruits_routes = Blueprint("devilFruits_routes",__name__)

# Devil fruits routes

@devilFruits_routes.route("/devilFruits",methods=['GET'])
def showAllDevilFruits():
    devilFruits = DevilFruit.allDevilFruits()
    return jsonify(devilFruits)

@devilFruits_routes.route("/devilFruit/<int:id>", methods=['GET'])
def showDevilFruit(id):
    devilFruit = DevilFruit.devilFruitById(id=id)
    return jsonify(devilFruit)
