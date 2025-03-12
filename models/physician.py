from flask_mysqldb import MySQL
from flask import jsonify
from database import db

class Physician(db.Model):
    __tablename__ = 'physicians'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True) 
    phone = db.Column(db.String(255), nullable=False, unique=True)  
    address = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Integer, nullable=False)    
    specialization_id = db.Column(db.Integer, db.ForeignKey('specializations.id', ondelete="CASCADE"), nullable=False)
    education_id = db.Column(db.Integer, db.ForeignKey('educations.id', ondelete="CASCADE"), nullable=False)

    specialization = db.relationship('Specialization', backref='physician_list')
    education = db.relationship('Education', backref='physician_list')

    def __init__(self, name, email, phone, address, gender, specialization_id, education_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address  
        self.gender = gender
        self.specialization_id = specialization_id
        self.education_id = education_id
