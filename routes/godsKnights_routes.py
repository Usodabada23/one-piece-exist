from flask import Flask, Blueprint,jsonify,request
from Model.GodsKnight import GodsKnight
import datetime
godsKnights_routes = Blueprint("godsKnights_routes",__name__)

# Gods Knights routes

@godsKnights_routes.route("/godsKnights",methods=['GET'])
def showAllGodsKnights():
    godsknights = GodsKnight.allGodsKnights()
    return jsonify(godsknights)

@godsKnights_routes.route("/godsKnight/<int:id>", methods=['GET'])
def showGodsknightById(id):
    godknight = GodsKnight.godknightById(id=id)
    return jsonify(godknight)

@godsKnights_routes.route("/godsKnight/add", methods=['POST'])
def addGodsKnight():
    try:

        data = request.get_json()

        required_fields = ["name", "godFamily", "weapon"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"The field '{field}' is missing."}), 400

        
        devilFruit_id = data.get("devilFruit_id", None)
        if devilFruit_id is not None:
            devilFruit_id = int(devilFruit_id)


        newGodKnight = GodsKnight(name=data["name"],godFamily=data["godFamily"],weapon=data["weapon"],devilFruit_id=devilFruit_id)

        newGodKnight.add()

        return jsonify({"message": "✅ God knight added successfully!"}), 201

    except ValueError as ve:
        return jsonify({"error": f"Format error: {str(ve)}"}), 400

    except Exception as e:
        return jsonify({"error": f"Error adding god knight: {str(e)}"}), 500

@godsKnights_routes.route("/godsKnight/<int:id>/delete", methods=['DELETE'])
def deleteGodsKnight(id):
    try:
        deleted = GodsKnight.delete(id=id)
        if deleted:
            return "", 204
        else:
            return jsonify({"error": "Devil Fruit not found"}), 404
    except ValueError as ve:
        return jsonify({"error": f"Format error: {str(ve)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Error deleting devil fruits: {str(e)}"}), 500
