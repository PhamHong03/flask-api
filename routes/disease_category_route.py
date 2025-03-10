from flask import Blueprint, request, jsonify
from controllers.disease_category_controller import DiseaseCategoryControllers

disease_category_bp = Blueprint('disease_category_bp', __name__)

@disease_category_bp.route('/disease_categories', methods=['GET'])
def get_disease_type():
    disease_category = DiseaseCategoryControllers.get_diseases_type()
    return jsonify([
        {"id": disease.id, 
         "name_category_disease": disease.name_category_disease, 
         "description_category_disease": disease.description_category_disease} 
        for disease in disease_category
    ]) 