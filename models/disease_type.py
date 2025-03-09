from flask_mysqldb import MySQL
from flask import jsonify
from database import db

class DiseaseCategory(db.Model):
    __tablename__ = 'disease_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_category_disease = db.Column(db.String(100), nullable=False, unique=True)
    description_category_disease = db.Column(db.String(255), nullable=False, unique=True)

    
    def __init__(self, name_category_disease, description_category_disease):
        self.name_category_disease = name_category_disease
        self.description_category_disease = description_category_disease