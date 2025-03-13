from flask import Blueprint, request, jsonify
from controllers.patient_controller import PatientController

patient_bp = Blueprint('patient_bp', __name__)

@patient_bp.route('/patients', methods=['GET'])
def get_all_patient():
    patients = PatientController.get_all_patient()

    if not patients:
        return jsonify({"message": "No patients found"}), 404

    return jsonify([
        { 
            "id": p.id,
            "name": p.name,
            "dateofbirth": p.dateofbirth,
            "gender" : p.gender,
            "phone": p.phone,
            "email": p.email,
            "job": p.job,
            "medical_code_card": p.medical_code_card,
            "code_card_day_start": p.code_card_day_start,
            "status": p.status
        }
        for p in patients   ]), 200

@patient_bp.route('/patients/<int:patient_id>', methods=['GET'])    
def get_patient(patient_id):
    patient = PatientController.get_patient_by_id(patient_id)
    if patient is None:
        return jsonify({"message": "Patient not found"}), 404

    return jsonify({
        "id": patient.id,
        "name": patient.name,
        "dateofbirth": patient.dateofbirth,
        "gender" : patient.gender,
        "phone": patient.phone,
        "email": patient.email,
        "job": patient.job,
        "medical_code_card": patient.medical_code_card,
        "code_card_day_start": patient.code_card_day_start,
        "status": patient.status
    }), 200

@patient_bp.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    new_patient = PatientController.create_patient(data)
    return jsonify({
        "id": new_patient.id,
        "name": new_patient.name,
        "dateofbirth": new_patient.dateofbirth, 
        "gender": new_patient.gender,
        "phone": new_patient.phone,
        "email": new_patient.email,
        "job": new_patient.job,
        "medical_code_card": new_patient.medical_code_card,
        "code_card_day_start": new_patient.code_card_day_start,
        "status": new_patient.status
    }), 201