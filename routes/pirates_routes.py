from flask import Flask, Blueprint,jsonify,request
from Model.Pirate import Pirate
import datetime
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

@pirates_routes.route("/pirate/add", methods=['POST'])
def addPirate():
    try:

        data = request.get_json()

        required_fields = ["name", "age", "height", "birthDate", "bounty", "weapon", "devilFruit_id", "was_supernova"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"The field '{field}' is missing."}), 400

        birthDate = datetime.datetime.strptime(data["birthDate"], "%Y-%m-%d").date()

        devilFruit_id = data.get("devilFruit_id", None)
        if devilFruit_id is not None:
            devilFruit_id = int(devilFruit_id)

        newPirate = Pirate(
            name=data["name"],
            age=int(data["age"]),
            height=int(data["height"]),
            birthDate=birthDate,
            bounty=int(data["bounty"]),
            weapon=data["weapon"],
            devilFruit_id=devilFruit_id,
            was_supernova=bool(data["was_supernova"])
        )

        newPirate.add()

        return jsonify({"message": "✅ Pirate added successfully!"}), 201

    except ValueError as ve:
        return jsonify({"error": f"Format error: {str(ve)}"}), 400

    except Exception as e:
        return jsonify({"error": f"Error adding pirate: {str(e)}"}), 500
    
@pirates_routes.route("/pirate/<int:id>/delete", methods=['DELETE'])
def deleteIsland(id):
    try:
        deleted = Pirate.delete(id=id)
        if deleted:
            return "", 204
        else:
            return jsonify({"error": "Pirate not found"}), 404
    except ValueError as ve:
        return jsonify({"error": f"Format error: {str(ve)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Error deleting pirate: {str(e)}"}), 500