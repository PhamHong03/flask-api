from models.appointment_form import AppointmentForm
from models.application_form import ApplicationForm
from flask import jsonify
from database import db
from datetime import datetime

class AppointmentFormController:
    @staticmethod
    def get_appointment_forms():
        return AppointmentForm.query.all()
    
    @staticmethod
    def get_appointment_form_by_id(appointment_form_id):
        return AppointmentForm.query.get(appointment_form_id)
    
    def get_application_form_by_id(application_form_id):
        application_form = ApplicationForm.query.get(application_form_id)
        if not application_form:
            return jsonify({"error": "Application Form not found"}), 404
        return jsonify(application_form.to_dict()), 200
    

    @staticmethod
    def create_appointment_form(data):
        
        application_form_id = data.get('application_form_id', 0)
        if not ApplicationForm.query.get(application_form_id):
            return {"error": "Application form not found"}, 404

        new_appointment_form = AppointmentForm(
            description=data.get('description', ''),
            application_form_id=application_form_id
        )
        
        try:
            db.session.add(new_appointment_form)
            db.session.commit()
            return new_appointment_form
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500