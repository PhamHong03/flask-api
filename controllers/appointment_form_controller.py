from models.appointment_form import AppointmentForm
from database import db
from datetime import datetime

class AppointmentFormController:
    @staticmethod
    def get_appointment_forms():
        return AppointmentForm.query.all()
    
    @staticmethod
    def get_appointment_form_by_id(appointment_form_id):
        return AppointmentForm.query.get(appointment_form_id)
    
    @staticmethod
    def create_appointment_form(data):
        new_appointment_form = AppointmentForm(
            description=data.get('description', ''),
            application_form_id=data.get('application_form_id', 0)
        )
        db.session.add(new_appointment_form)
        db.session.commit()
        return new_appointment_form