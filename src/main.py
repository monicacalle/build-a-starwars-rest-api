"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from models import Character, Planet, Vehicle, Favorite

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route("/characters", methods=["GET"])
def get_characters():
    try:
        all_character = Character.query.all()
        all_characters = list(map(lambda character: character.serialize(), all_character))
        return jsonify(all_characters)
    except Exception as error:
        print(f"Character error : {error}")
        return jsonify({"msg": "error occurred"})    

@app.route("/planets", methods=["GET"])
def get_planets():
    try:
        all_planets = Planet.query.all()
        all_planets = list(map(lambda planets: planets.serialize(), all_planets))
        return jsonify(all_planets)
    except Exception as error:
        print(f"Planet error : {error}")
        return jsonify({"msg": "error occurred"})

@app.route("/vehicles", methods=["GET"])
def get_vehicles():
    try:
        all_vehicles = Vehicle.query.all()
        all_vehicles = list(map(lambda vehicles: vehicles.serialize(), all_starships))
        return jsonify(all_vehicles)
    except Exception as error:
        print(f"Vehicles error : {error}")
        return jsonify({"msg": "error occurred"})

@app.route("/favorite", methods=["GET"])
def get_favorite():
    try:
        all_favorite = Favorite.query.all()
        all_favorite = list(map(lambda favorite: favorite.serialize(), all_favorite))
        return jsonify(all_favorite)
    except Exception as error:
        print(f"Favorite error : {error}")
        return jsonify({"msg": "error occurred"})

@app.route("/favorite", methods=["POST"])
def create_favorite():
    try: 
        favorite = Favorite()
        body = request.get_json()
        favorite.favorito = body["favorito"]       
        db.session.add(favorite)
        db.session.commit()
        return jsonify({"favorite": body["favorito"]})
    except Exception as error:
        print(f"FavoritePOST error : {error}")
        return jsonify({"msg": "error occurred"})


@app.route("/favorite/<int:id>", methods=['DELETE'])
def delete_favorites(id):
    favorite = Favorite.query.filter_by(id=id)
    if favorite is None:
        return jsonify({"message": "Not Found"}), 404
    deleted = favorite.delete()
    if deleted == False:
        return jsonify({"message": "Something happen try again"}), 500
    return jsonify([]), 204

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=False)






