from flask import jsonify, request  
from database import db

from models.type_disease import Type_Disease

class TypeDiseaseController():

    @staticmethod
    def get_all_type_disease():
        return Type_Disease.query.all()
    
    @staticmethod
    def get_type_disease_by_id(type_disease_id):
        return Type_Disease.query.get(type_disease_id)
    
    @staticmethod
    def create_type_disease(data):
        new_type_disease = Type_Disease(type_disease_name=data['type_disease_name'], type_disease_description=data['type_disease_description'])
        db.session.add(new_type_disease)
        db.session.commit()
        return new_type_disease