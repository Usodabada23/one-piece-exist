from flask import Flask
from Model.Database import Database
from routes.pirates_routes import pirates_routes
from routes.marines_routes import marines_routes
from routes.islands_routes import islands_routes
from routes.godsKnights_routes import godsKnights_routes
from routes.devilFruits_routes import devilFruits_routes
from flask import jsonify
app = Flask(__name__)
@app.route("/")
def hello_world():
    db = Database()
    db.create_tables()  
    return "Hello, World! The One piece exist!"

# Pirates routes 
app.register_blueprint(pirates_routes)
# Marines routes
app.register_blueprint(marines_routes)
# Islands routes
app.register_blueprint(islands_routes)
# Gods Knights routes
app.register_blueprint(godsKnights_routes)
# Devil fruits routes
app.register_blueprint(devilFruits_routes)


if __name__ == "__main__":
    app.run(debug=True)
