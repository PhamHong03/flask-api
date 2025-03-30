from database import db
from datetime import datetime
from sqlalchemy.sql import func

class Images(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    images_path = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())  
    physician_id = db.Column(db.Integer, db.ForeignKey('physicians.id', ondelete="CASCADE"), nullable=False)
    appointment_form_id = db.Column(db.Integer, db.ForeignKey('appointment_forms.id', ondelete="CASCADE"), nullable=False)

    diagnose_disease_id = db.Column(db.Integer, db.ForeignKey('diagnose_disease.id', ondelete="CASCADE"), nullable=True)

    physician = db.relationship('Physician', back_populates='images')
    diagnose_disease = db.relationship('Diagnose_Disease', back_populates='images')

    appointment_form = db.relationship('AppointmentForm', back_populates='images')

    def __init__(self, images_path, physician_id, appointment_form_id, diagnose_diseases_id=None):
        self.images_path = images_path
        self.created_at = datetime.utcnow()
        self.physician_id = physician_id
        self.appointment_form_id = appointment_form_id
        self.diagnose_diseases_id = diagnose_diseases_id
