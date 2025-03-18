from models.application_form import ApplicationForm
from database import db

class ApplicationFormController:
    @staticmethod
    def get_application_forms():
        return ApplicationForm.query.all()

    @staticmethod
    def get_application_form_by_id(application_form_id):
        return ApplicationForm.query.get(application_form_id)

    @staticmethod
    def create_application_form(data):
        new_application_form = ApplicationForm(
            content=data.get('content', ''),
            application_form_date=data.get('application_form_date', 0),
            room_id=data.get('room_id', ''),
            patient_id=data.get('patient_id', 0),
            medical_history_id=data.get('medical_history_id', 0)
        )
        db.session.add(new_application_form)
        db.session.commit()
        return new_application_form

    @staticmethod
    def update_application_form(application_form_id, data):
        application_form = ApplicationForm.query.get(application_form_id)
        if not application_form:
            return None  

        application_form.content = data.get('content', application_form.content)
        application_form.application_form_date = data.get('application_form_date', application_form.application_form_date)
        application_form.room_id = data.get('room_id', application_form.room_id)
        application_form.patient_id = data.get('patient_id', application_form.patient_id)
        application_form.medical_history_id = data.get('medical_history_id', application_form.medical_history_id)

        db.session.commit()
        return application_form

    @staticmethod
    def delete_application_form(application_form_id):
        application_form = ApplicationForm.query.get(application_form_id)
        if not application_form:
            return None  

        db.session.delete(application_form)
        db.session.commit()
        return application_form
