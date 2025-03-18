from flask_mysqldb import MySQL
from flask import jsonify
from database import db

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    dateofbirth = db.Column(db.BigInteger, nullable=False) 
    gender = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(255), nullable=False, unique=True)
    job = db.Column(db.String(255), nullable=False)
    medical_code_card = db.Column(db.String(255), nullable=False)
    code_card_day_start = db.Column(db.BigInteger, nullable=False)  
    status = db.Column(db.Integer, nullable=False)

    # Quan hệ với ApplicationForm
    application_forms = db.relationship('ApplicationForm', back_populates='patient', cascade="all, delete-orphan")

    def __init__(self, name, dateofbirth, gender, email, phone, job, medical_code_card, code_card_day_start, status):
        self.name = name
        self.dateofbirth = dateofbirth
        self.gender = gender
        self.email = email
        self.phone = phone
        self.job = job
        self.medical_code_card = medical_code_card
        self.code_card_day_start = code_card_day_start
        self.status = status