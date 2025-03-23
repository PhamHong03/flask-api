from database import db

class AppointmentForm(db.Model):
    __tablename__ = 'appointment_forms'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(255), nullable=False)
    application_form_id = db.Column(db.Integer, db.ForeignKey('application_forms.id', ondelete="CASCADE"), nullable=False)

    application_form = db.relationship('ApplicationForm', back_populates='appointment_forms')

    def __init__(self, description, application_form_id):
        self.description = description
        self.application_form_id = application_form_id