from database import db

class MedicalHistory(db.Model):
    __tablename__ = 'medical_histories'  

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255), nullable=False)
    physician_id = db.Column(db.Integer, db.ForeignKey('physicians.id', ondelete="CASCADE"), nullable=False)
    calendar_date = db.Column(db.Date, nullable=False)

    physician = db.relationship('Physician', back_populates='medical_histories')
    application_forms = db.relationship('ApplicationForm', back_populates='medical_history', cascade="all, delete-orphan")

    def __init__(self, description,  physician_id, calendar_date):
        self.description = description
        self.physician_id = physician_id
        self.calendar_date = calendar_date