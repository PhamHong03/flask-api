from models.images import Images
from database import db
from datetime import datetime

class ImagesController:
    @staticmethod
    def get_images():
        return Images.query.all()
    
    @staticmethod
    def get_image_by_id(image_id):
        return Images.query.get(image_id)
    @staticmethod
    def get_images_by_appointment_id(appointment_id):
        return Images.query.filter_by(appointment_id=appointment_id).all()
    @staticmethod
    def create_image(data):
        try:
            new_image = Images(
                images_path=data['images_path'], 
                physician_id=data['physician_id'],
                appointment_id=data['appointment_id'],
                diagnose_disease_id=data.get('diagnose_disease_id')  
            )
            db.session.add(new_image)
            db.session.commit()
            return new_image, None  
        
        except Exception as e:
            db.session.rollback() 
            return None, str(e)
