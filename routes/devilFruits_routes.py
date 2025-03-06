from flask import Flask, Blueprint,jsonify,request
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

@devilFruits_routes.route("/island/add", methods=['POST'])
def addDevilFruit():
    try:

        data = request.get_json()

        required_fields = ["name", "type", "description","ability","rarity","is_eaten"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"The field '{field}' is missing."}), 400

        


        newDevilFruit = DevilFruit(name=data["name"],typeFruit=data["type"],description=data["description"],
                                   ability=data["ability"],rarity=data["rarity"],isEaten=data["is_eaten"])

        newDevilFruit.add()

        return jsonify({"message": "✅ Devil Fruit added successfully!"}), 201

    except ValueError as ve:
        return jsonify({"error": f"Format error: {str(ve)}"}), 400

    except Exception as e:
        return jsonify({"error": f"Error adding pirate: {str(e)}"}), 500