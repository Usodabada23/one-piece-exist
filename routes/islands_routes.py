from flask import Flask, Blueprint,jsonify,request
from Model.Island import Island
import datetime
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
@islands_routes.route("/island/add", methods=['POST'])
def addIsland():
    try:

        data = request.get_json()

        required_fields = ["name", "location", "government"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"The field '{field}' is missing."}), 400

        
        affiliated_group = data.get("affiliated_group", None)
        if affiliated_group is not None:
            affiliated_group = int(affiliated_group)


        newIsland = Island(name=data["name"],location=data["location"],government=data["government"],affiliated_group=affiliated_group)

        newIsland.add()

        return jsonify({"message": "✅ Island added successfully!"}), 201

    except ValueError as ve:
        return jsonify({"error": f"Format error: {str(ve)}"}), 400

    except Exception as e:
        return jsonify({"error": f"Error adding island: {str(e)}"}), 500