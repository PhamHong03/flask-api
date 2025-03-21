from models.medical_history import MedicalHistory
from database import db
from datetime import datetime

class MedicalHistoryController:
    @staticmethod
    def get_medical_histories():
        return MedicalHistory.query.all()
    
    @staticmethod   
    def get_medical_history_by_id(id):
        return MedicalHistory.query.get(id)
    
    @staticmethod
    def create_medical_history(medical_history):
        new_medical_history = MedicalHistory(
            description=medical_history['description'],
            physician_id=medical_history['physician_id'],
            calendar_date=datetime.strptime(medical_history.get('application_form_date', ''), "%Y-%m-%d").date()
            )
        db.session.add(new_medical_history)
        db.session.commit()
        return new_medical_history
    