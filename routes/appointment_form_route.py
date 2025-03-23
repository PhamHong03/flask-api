from flask import Blueprint, request, jsonify
from controllers.appointment_form_controller import AppointmentFormController

appointment_form_bp = Blueprint('appointment_form_bp', __name__)
@appointment_form_bp.route('/appointment-forms', methods=['GET'])
def get_appointment_forms():
    appointment_forms = AppointmentFormController.get_appointment_forms()

    if not appointment_forms:
        return jsonify({"message": "No appointment forms found"}), 404
    return jsonify([
        {
            "id": af.id,
            "description": af.description,
            "application_form_id": af.application_form_id
        }
        for af in appointment_forms]), 200

@appointment_form_bp.route('/appointment-forms/<int:appointment_form_id>', methods=['GET']) 
def get_appointment_form(appointment_form_id):
    appointment_form = AppointmentFormController.get_appointment_form_by_id(appointment_form_id)
    if appointment_form is None:
        return jsonify({"message": "Appointment form not found"}), 404
    return jsonify({
        "id": appointment_form.id,
        "description": appointment_form.description,
        "application_form_id": appointment_form.application_form_id
    }), 200

@appointment_form_bp.route('/appointment-forms', methods=['POST'])
def create_appointment_form():
    data = request.get_json()
    if not data or 'description' not in data or 'application_form_id' not in data:
        return jsonify({"message": "Missing required fields"}), 400

    new_appointment_form = AppointmentFormController.create_appointment_form(data)
    return jsonify({
        "id": new_appointment_form.id,
        "description": new_appointment_form.description,
        "application_form_id": new_appointment_form.application_form_id
    }), 201