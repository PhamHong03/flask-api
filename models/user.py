from flask_mysqldb import MySQL
from flask import jsonify
from database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, phone, email, password):
        self.user_name = name
        self.phone_number = phone
        self.email = email
        self.password = password
