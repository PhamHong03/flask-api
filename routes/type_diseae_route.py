from flask import Blueprint, request, jsonify
from controllers.type_disease_controller import TypeDiseaseController   

type_disease_bp = Blueprint('type_disease_bp', __name__)

@type_disease_bp.route('/type_disease', methods=['GET'])    
def get_all_type_disease():
    type_diseases = TypeDiseaseController.get_all_type_disease()
    return jsonify([{"id":t.id, "type_disease_name": t.type_disease_name, "type_disease_description": t.type_disease_description} for t in type_diseases])

@type_disease_bp.route('/type_diseases/<int:type_disease_id>', methods=['GET']) 
def get_type_disease_by_id(type_disease_id):
    type_disease = TypeDiseaseController.get_type_disease_by_id(type_disease_id)
    return jsonify({"id":type_disease.id, "type_disease_name": type_disease.type_disease_name, "type_disease_description": type_disease.type_disease_description})  