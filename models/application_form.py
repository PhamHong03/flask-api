from database import db

class ApplicationForm(db.Model):
    __tablename__ = 'application_forms'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(255), nullable=False)
    application_form_date = db.Column(db.Date, nullable=False)

    room_id = db.Column(db.String(255), db.ForeignKey('room.id', ondelete="CASCADE"), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id', ondelete="CASCADE"), nullable=False)
    medical_history_id = db.Column(db.Integer, db.ForeignKey('medical_histories.id', ondelete="CASCADE"), nullable=False)

    room = db.relationship('Room', back_populates='application_forms')
    patient = db.relationship('Patient', back_populates='application_forms')
    medical_history = db.relationship('MedicalHistory', back_populates='application_forms')

    appointment_forms = db.relationship('AppointmentForm', back_populates='application_form', cascade="all, delete-orphan")


    def __init__(self, content, application_form_date, room_id, patient_id, medical_history_id):
        self.content = content
        self.application_form_date = application_form_date
        self.room_id = room_id
        self.patient_id = patient_id
        self.medical_history_id = medical_history_id


    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "application_form_date": self.application_form_date.strftime("%Y-%m-%d"),
            "room_id": self.room_id,
            "patient_id": self.patient_id,
            "medical_history_id": self.medical_history_id
        }