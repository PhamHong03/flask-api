from flask import Blueprint, request, jsonify
from controllers.application_form_controller import ApplicationFormController


application_form_bp = Blueprint('application_form_bp', __name__)    
@application_form_bp.route('/application_forms', methods=['GET'])
def get_application_forms():    
    application_forms = ApplicationFormController.get_application_forms()

    if not application_forms:
        return jsonify({"message": "No application forms found"}), 404  
    return jsonify([
        {
            "id" : af.id,
            "content": af.content,
            "application_form_date": af.application_form_date,
            "room_id": af.room_id,
            "patient_id": af.patient_id,
            "medical_history_id": af.medical_history_id
        }
        for af in application_forms]), 200
    
@application_form_bp.route('/application_forms/<int:application_form_id>', methods=['GET'])
def get_application_form(application_form_id):
    application_form = ApplicationFormController.get_application_form_by_id(application_form_id)
    if application_form is None:
        return jsonify({"message": "Application form not found"}), 404
    return jsonify({
        "id" : application_form.id,
        "content": application_form.content,
        "application_form_date": application_form.application_form_date,
        "room_id": application_form.room_id,
        "patient_id": application_form.patient_id,
        "medical_history_id": application_form.medical_history_id
    }), 200


@application_form_bp.route('/application_forms', methods=['POST'])
def create_application_form():
    data = request.get_json()
    if not data or 'content' not in data or 'room_id' not in data:
        return jsonify({"message": "Missing required fields"}), 400

    new_application_form = ApplicationFormController.create_application_form(data)
    return jsonify({
        "id": new_application_form.id,
        "content": new_application_form.content,
        "application_form_date": new_application_form.application_form_date,
        "room_id": new_application_form.room_id,
        "patient_id": new_application_form.patient_id,
        "medical_history_id": new_application_form.medical_history_id
    }), 201