from models.physician import Physician
from database import db 

class PhysicianController:
    @staticmethod
    def get_all_physician():
        return Physician.query.all()
    
    @staticmethod
    def get_physician_by_id(physician_id):
        return Physician.query.get(physician_id)
    
    @staticmethod
    def create_physician(data):
        print("Data from Android:", data)
        new_physician = Physician(
            name=data['name'], 
            email=data['email'], 
            phone=data['phone'], 
            address=data['address'],
            gender=data['gender'] , 
            specialization_id=data['specialization_id'],
            education_id=data['education_id']
        )

        db.session.add(new_physician)
        db.session.commit()
        return new_physician