from flask import Blueprint, request, jsonify   
from controllers.physician_controller import PhysicianController
from models.physician import Physician

physician_bp = Blueprint('physician_bp', __name__)

@physician_bp.route('/physicians', methods=['GET'])
def get_all_physician():
    physicians = PhysicianController.get_all_physician()

    if not physicians:
        return jsonify({"message": "No physicians found"}), 404

    return jsonify([
        {
            "id": p.id, 
            "name": p.name, 
            "email": p.email, 
            "phone": p.phone, 
            "address": p.address,
            "gender": p.gender,
            "specialization_id": p.specialization_id,
            "education_id": p.education_id,
            "account_id": p.account_id
        }
        for p in physicians
    ]), 200  

@physician_bp.route('/physicians/<int:physician_id>', methods=['GET'])  
def get_physician(physician_id):
    physician = PhysicianController.get_physician_by_id(physician_id) 
    if physician is None:
        return jsonify({"message": "Physician not found"}), 404

    return jsonify({
        "id": physician.id, 
        "name": physician.name, 
        "email": physician.email, 
        "phone": physician.phone, 
        "address": physician.address,
        "gender": physician.gender,
        "specialization_id": physician.specialization_id,
        "education_id": physician.education_id,
        "account_id": physician.account_id
    }), 200


@physician_bp.route('/physicians', methods=['POST'])
def create_physician():
    data = request.get_json()
    print("Received data from Android:", data)
    new_physician = PhysicianController.create_physician(data)
    return jsonify({
        "id": new_physician.id,
        "name": new_physician.name,
        "email": new_physician.email,
        "phone": new_physician.phone,
        "address": new_physician.address,
        "gender": new_physician.gender,
        "specialization_id": new_physician.specialization_id,
        "education_id": new_physician.education_id,
        "account_id": new_physician.account_id
    }), 201
        
@physician_bp.route('/physicians/account/<int:account_id>', methods=['GET'])
def get_physicians_by_account_id(account_id):
    physician = Physician.query.filter_by(account_id=account_id).first()
    if not physician:
        return jsonify({"message": "Physician not found"}), 404
    
    return jsonify({
        "id": physician.id,
        "name": physician.name,
        "email": physician.email,
        "phone": physician.phone,
        "address": physician.address,
        "gender": physician.gender,
        "specialization_id": physician.specialization_id,
        "education_id": physician.education_id,
        "account_id": physician.account_id
    }), 200