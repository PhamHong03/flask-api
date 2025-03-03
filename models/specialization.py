from flask_mysqldb import MySQL
from flask import jsonify
from database import db

# mysql = MySQL()

class Specialization(db.Model):
    __tablename__ = 'specializations'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    quantity_patient = db.Column(db.Integer, nullable=False)

    def __init__(self, name):
        self.name = name