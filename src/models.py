from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(120), unique=True, nullable=False)
     email = db.Column(db.String(120), unique=True, nullable=False)
    
     def __repr__(self):
        return '<User %r>' % self.id

     def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
class Planets(db.Model):
    __tablename__= 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    terrain = db.Column(db.String(200))
    climate = db.Column(db.String(200))
    description = db.Column(db.String(500))
    
    def __repr__(self):
        return '<Planets %r>' % self.planets

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "climate": self.climate,
            "description": self.description
        }
class Characters(db.Model):
    __tablename__= 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    birth_year = db.Column(db.String(150), nullable=False)
    eye_color = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(150), nullable=False)
    hair_color = db.Column(db.String(150), nullable=False)
    height = db.Column(db.String(200), nullable=False)
    homeworld = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return '<Characters %r>' % self.characters

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "homeworld": self.homeworld,
        }
class Vehicles(db.Model):
    __tablename__= 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(150), nullable=False)
    manufacturer = db.Column(db.String(200), nullable=False)
    class_vehícle = db.Column(db.String(200), nullable=False)
    maximum_atmospheric_speed = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Vehicles %r>' % self.vehicles

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "class_vehicle": self.class_vehícle,
            "maximum atmospheric speed": self.maximum_atmospheric_speed
        }

class Favorites(db.Model):
    __tablename__= 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"))
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"))
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicles.id"))

    def __repr__(self):
        return '<Favorites %r>' % self.favorites

    def serialize(self):
        return {
            "id": self.id,
            "planet_id": self.planets_id,
            "character_id": self.character_id,
            "vehicles_id": self.vehicle_id,
        }