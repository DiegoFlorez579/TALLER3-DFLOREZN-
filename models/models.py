from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()

# Definir los modelos:

class Usuarios(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    es_admin = db.Column(db.Boolean(), default = False)

class Perros(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    raza = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    peso = db.Column(db.Float)