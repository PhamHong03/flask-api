from flask import Blueprint, request, jsonify
from controllers.patient_controller import PatientController
from models.patient import Patient

patient_bp = Blueprint('patient_bp', __name__)

@patient_bp.route('/patients', methods=['GET'])
def get_all_patient():
    patients = PatientController.get_all_patient()

    if not patients:
        return jsonify({"message": "Không có bệnh nhân nào"}), 404

    return jsonify([
        { 
            "id": p.id,
            "name": p.name,
            "day_of_birth": p.day_of_birth.strftime("%Y-%m-%d"),  
            "gender" : p.gender,
            "phone": p.phone,
            "email": p.email,
            "job": p.job,
            "medical_code_card": p.medical_code_card,
            "code_card_day_start": p.code_card_day_start.strftime("%Y-%m-%d"),  
            "status": p.status,
            "account_id": p.account_id
        }
        for p in patients  
    ]), 200

@patient_bp.route('/patients/<int:patient_id>', methods=['GET'])    
def get_patient(patient_id):
    patient = PatientController.get_patient_by_id(patient_id)
    if not patient:
        return jsonify({"message": "Không tìm thấy bệnh nhân"}), 404

    return jsonify({
        "id": patient.id,
        "name": patient.name,
        "day_of_birth": patient.day_of_birth.strftime("%Y-%m-%d"),  
        "gender" : patient.gender,
        "phone": patient.phone,
        "email": patient.email,
        "job": patient.job,
        "medical_code_card": patient.medical_code_card,
        "code_card_day_start": patient.code_card_day_start.strftime("%Y-%m-%d"),  
        "status": patient.status,
        "account_id": patient.account_id
    }), 200

@patient_bp.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()

    required_fields = ["name", "day_of_birth", "gender", "email", "phone", "job", "medical_code_card", "code_card_day_start", "status", "account_id"]
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"message": "Thiếu thông tin: " + ", ".join(missing_fields)}), 400

    new_patient, error = PatientController.create_patient(data)
    if error:
        return jsonify({"message": error}), 400

    return jsonify({
        "id": new_patient.id,
        "name": new_patient.name,
        "day_of_birth": new_patient.day_of_birth.strftime("%Y-%m-%d"),  
        "gender": new_patient.gender,
        "phone": new_patient.phone,
        "email": new_patient.email,
        "job": new_patient.job,
        "medical_code_card": new_patient.medical_code_card,
        "code_card_day_start": new_patient.code_card_day_start.strftime("%Y-%m-%d"),  
        "status": new_patient.status,
        "account_id": new_patient.account_id
    }), 201



@patient_bp.route('/patients/account/<int:account_id>', methods=['GET'])
def get_patient_by_account(account_id):
    patient = Patient.query.filter_by(account_id=account_id).first()
    
    if not patient:
        return jsonify({"message": "Patient not found"}), 404

    return jsonify({
        "id": patient.id,
        "name": patient.name,
        "day_of_birth": patient.day_of_birth.strftime("%Y-%m-%d"),  
        "gender": patient.gender,
        "phone": patient.phone,
        "email": patient.email,
        "job": patient.job,
        "medical_code_card": patient.medical_code_card,
        "code_card_day_start": patient.code_card_day_start.strftime("%Y-%m-%d"),  
        "status": patient.status,
        "account_id": patient.account_id
    }), 200
