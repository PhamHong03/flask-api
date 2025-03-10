from database import db
from flask_bcrypt  import  Bcrypt   


class Type_Disease(db.Model):
    __tablename__ = 'type_disease'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    type_disease_name = db.Column(db.String(255), nullable=False)
    type_disease_description = db.Column(db.String(255), nullable=False)
    
       
    def __init__(self, type_disease_name, type_disease_description):
        self.type_disease_name = type_disease_name
        self.type_disease_description = type_disease_description