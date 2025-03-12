from flask_mysqldb import MySQL
from flask import jsonify
from database import db

#mysql = MySQL()

class Education(db.Model):
    __tablename__ = 'educations'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    
    # Quan hệ với Physician
    physicians = db.relationship('Physician', backref='education', lazy=True)
    
    def __init__(self, name):
        self.name = name