from flask import jsonify, request
from database import db
from models.disease_type import DiseaseCategory

class DiseaseCategoryControllers():

    @staticmethod
    def get_diseases_type():
        return DiseaseCategory.query.all()
    
    @staticmethod
    def get_disease_type_by_id(disease_id):

        return DiseaseCategory.query.filter_by(id=disease_id).first()
    
    @staticmethod 
    def create_disease_type(data):
        new_disease_type = DiseaseCategory(
            name_category_disease=data['name_category_disease'], 
            description_category_disease=data['description_category_disease']
        )
        db.session.add(new_disease_type)
        db.session.commit()
        return new_disease_type