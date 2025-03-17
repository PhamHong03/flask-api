from database import db

class MedicalHistory(db.Model):
    __tablename__ = 'medical_histories'  

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255), nullable=False)
    physician_id = db.Column(db.Integer, db.ForeignKey('physicians.id', ondelete="CASCADE"), nullable=False)

    physician = db.relationship('Physician', back_populates='medical_histories')

    def __init__(self, description, physician_id):
        self.description = description
        self.physician_id = physician_id