from flask import Flask, Blueprint,jsonify,request
from Model.Marine import Marine
import datetime

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

@marines_routes.route("/marine/add", methods=['POST'])
def addMarine():
    try:

        data = request.get_json()

        required_fields = ["name", "age", "height", "weapon", "rank"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"The field '{field}' is missing."}), 400

        
        devilFruit_id = data.get("devilFruit_id", None)
        if devilFruit_id is not None:
            devilFruit_id = int(devilFruit_id)

        cgbounty = data.get("cgbounty",None)
        if cgbounty is not None:
            cgbounty = int(cgbounty)


        newMarine = Marine(name=data["name"],age=int(data["age"]),height=int(data["height"]),
                           cgbounty=cgbounty,weapon=data["weapon"],devilFruit_id=devilFruit_id,rank=data["rank"])

        newMarine.add()

        return jsonify({"message": "✅ Marine added successfully!"}), 201

    except ValueError as ve:
        return jsonify({"error": f"Format error: {str(ve)}"}), 400

    except Exception as e:
        return jsonify({"error": f"Error adding marine: {str(e)}"}), 500