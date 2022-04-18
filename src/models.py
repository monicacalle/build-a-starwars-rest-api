from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),nullable=False)
    nickname = db.Column(db.String(250),nullable=False)
    email = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(250),nullable=False)

    def __repr__ (self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "nickname": self.nickname,
            "email": self.email,
            # "password": self.password,
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(30), nullable=False)
    dob = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __repr__ (self):
        return '<Character %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "dob": self.dob,
            "user_id": self.user_id,
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    weather = db.Column(db.Integer, nullable=False)
    gravity =  db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __repr__ (self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "weather": self.weather,
            "gravity": self.gravity,
            "population": self.population,
            "user_id": self.user_id,
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    vehicle_class = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.ForeignKey('user.id'))

    def __repr__ (self):
        return '<Vehicle %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "vehicle_class": self.vehicle_class,
            "manufacturer": self.manufacturer,
            "cargo_capacity": self.cargo_capacity,
            "user_id": self.user_id,
            
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite = db.Column(db.String(250))

    def __repr__ (self):
        return '<Favorite %r>' % self.favorite

    def serialize(self):
        return {
            "favorite" : self.Favorite
        }