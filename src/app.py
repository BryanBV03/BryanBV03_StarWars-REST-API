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
from models import db, User, Planets, Characters, Vehicles, Favorites
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
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



# =========METODOS GET:
@app.route('/user', methods=['GET'])
def get_user():
    all_user = User.query.all()
    result = [element.serialize() for element in all_user]
    response_body = {
        "msg": "All good, you got users!!!",
        "user": result
    }
    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def get_planets():
    all_planets = Planets.query.all()
    result = [element.serialize() for element in all_planets]
    response_body = {
        "msg": "All good, you got planets!!!",
        "planets": result
    }
    return jsonify(response_body), 200

@app.route('/characters', methods=['GET'])
def get_characters():
    all_characters = Characters.query.all()
    result = [element.serialize() for element in all_characters]
    response_body = {
        "msg": "All good, you got characters!!!",
        "characters": result
    }
    return jsonify(response_body), 200

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    all_vehicles = Vehicles.query.all()
    result = [element.serialize() for element in all_vehicles]
    response_body = {
        "msg": "All good, you got vehicles!!!",
        "vehicles": result
    }
    return jsonify(response_body), 200

@app.route('/favorites', methods=['GET'])
def get_favorites():
    all_favorites = Favorites.query.all()
    result = [element.serialize() for element in all_favorites]
    response_body = {
        "msg": "All good, you got favorites!!!",
        "favorites": result
    }
    return jsonify(response_body), 200



# ========METODOS GET * ID:
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_id(user_id):
    user = User.query.get(user_id)
    result = user.serialize()
    response_body = {
        "msg": "User received",
        "user": result
    }
    return jsonify(response_body), 200    
@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_planets_id(planets_id):
    planet = Planets.query.get(planets_id)
    result = planet.serialize()
    response_body = {
        "msg": "Pla recibido",
        "user": result
    }
    return jsonify(response_body), 200   
 
@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character_id(characters_id):
    character = Characters.query.get(characters_id)
    result = character.serialize()
    response_body = {
        "msg": "Character received",
        "character": result
    }
    return jsonify(response_body), 200 
   
@app.route('/vehicles/<int:vehicles_id>', methods=['GET'])
def get_vehicles_id(vehicles_id):
    vehicle = Vehicles.query.get(vehicles_id)
    result = vehicle.serialize()
    response_body = {
        "msg": "Vehicle received",
        "vehicle": result
    }
    return jsonify(response_body), 200  


# ==========METODOS POST:
@app.route('/users', methods=['POST'])
def createUser():
    data = request.data
    data = json.loads(data)
    newUser = User(name = data["name"], email = data["email"], id = data["id"])
    db.session.add(newUser)
    db.session.commit()

    return jsonify(newUser.serialize())

@app.route('/planets', methods=['POST'])
def createPlanet():
    data = request.data
    data = json.loads(data)
    newPlanet = Planets(id = data["id"], name = data["data"], terrain = data["terrain"], climate = data["climate"], description = data["description"])
    db.session.add(newPlanet)
    db.session.commit()

    return jsonify(newPlanet.serialize())

@app.route('/characters', methods=['POST'])
def createCharacter():
    data = request.data
    data = json.loads(data)
    newCharacter = Characters(id = data["id"], name = data["data"], birth_year = data["birth_year"], eye_color = data["eye_color"], gender = data["gender"], hair_color = data["hair_color"], height = data["height"], homeworld = data["homeworld"])
    db.session.add(newCharacter)
    db.session.commit()

    return jsonify(newCharacter.serialize())

@app.route('/vehicles', methods=['POST'])
def createVehicle():
    data = request.data
    data = json.loads(data)
    newVehicle = Vehicles(id = data["id"], name = data["data"], model = data["model"], manufacturer = data["manufacturer"], class_vehícle = data["class_vehícle"], maximum_atmospheric_speed = data["maximum_atmospheric_speed"])
    db.session.add(newVehicle)
    db.session.commit()

    return jsonify(newVehicle.serialize())

# ===========METODOS DELETE:


@app.route('/users/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({"msg": "User successfully eliminated"}), 200

@app.route('/planets/<int:planet_id>', methods=['DELETE'])
def deletePlanet(planet_id):
    planet = Planets.query.get(planet_id)
    if planet is None:
        return jsonify({"error": "Planet not found"}), 404
    
    db.session.delete(planet)
    db.session.commit()
    return jsonify({"msg": "planet successfully eliminated"}), 200

@app.route('/characters/<int:character_id>', methods=['DELETE'])
def deleteCharacter(character_id):
    character = Characters.query.get(character_id)
    if character is None:
        return jsonify({"error": "Character not found"}), 404
    
    db.session.delete(character)
    db.session.commit()
    return jsonify({"msg": "character successfully eliminated"}), 200

@app.route('/vehicles/<int:vehicles_id>', methods=['DELETE'])
def deleteVehicle(vehicle_id):
    vehicle = Vehicles.query.get(vehicle_id)
    if vehicle is None:
        return jsonify({"error": "Vehicle not found"}), 404
    
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({"msg": "Vehicle successfully eliminated"}), 200






# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
