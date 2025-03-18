from flask import Blueprint, request, jsonify
from controllers.medical_history_controller import MedicalHistoryController 

medical_history_bp = Blueprint('medical_history_bp', __name__)  

@medical_history_bp.route('/medical_histories', methods=['GET'])    
def get_medical_histories():
    medical_histories = MedicalHistoryController.get_medical_histories()
    
    if not medical_histories:
        return jsonify({"message": "No medical histories found"}), 404
    
    return jsonify([
        {
            "id": mh.id,
            "description": mh.description,
            "physician_id": mh.physician_id
        }
        for mh in medical_histories
    ]), 200

@medical_history_bp.route('/medical_histories/<int:id>', methods=['GET'])   
def get_medical_history(id):
    try:
        medical_history = MedicalHistoryController.get_medical_history_by_id(id)

        if not medical_history:
            return jsonify({"message": "No medical history found"}), 404
        
        return jsonify({
            "id": medical_history.id,
            "description": medical_history.description,
            "physician_id": medical_history.physician_id
        }), 200
    except Exception as e:
        return jsonify({"message": "Internal Server Error", "error": str(e)}), 500


@medical_history_bp.route('/medical_histories', methods=['POST'])
def create_medical_history():
    data = request.get_json()
    if not data or 'description' not in data or 'physician_id' not in data:
        return jsonify({"message": "Missing required fields"}), 400

    new_medical_history = MedicalHistoryController.create_medical_history(data)
    return jsonify({
        "id": new_medical_history.id,
        "description": new_medical_history.description,
        "physician_id": new_medical_history.physician_id
    }), 201