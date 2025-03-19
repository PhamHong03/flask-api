from models.patient import Patient
from database import db
from datetime import datetime

class PatientController:
    @staticmethod
    def get_all_patient():
        return Patient.query.all()
    
    @staticmethod
    def get_patient_by_id(patient_id):
        return Patient.query.get(patient_id)
    
    @staticmethod
    def create_patient(data):
        new_patient = Patient(
            name=data['name'],
            day_of_birth=datetime.strptime(data['day_of_birth'], "%Y-%m-%d").date(),  
            gender=data['gender'],
            email=data['email'],
            phone=data['phone'],
            job=data['job'],
            medical_code_card=data['medical_code_card'],
            code_card_day_start=datetime.strptime(data['code_card_day_start'], "%Y-%m-%d").date(),  
            status=data['status']
        )
        db.session.add(new_patient)
        db.session.commit()
        return new_patient