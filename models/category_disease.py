from database import db
from flask_bcrypt  import  Bcrypt   


class Category_Disease(db.Model):
    __tablename__ = 'category_disease'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    category_disease_name = db.Column(db.String(255), nullable=False)
    category_disease_description = db.Column(db.String(255), nullable=False)
    
       
    def __init__(self, category_disease_name, category_disease_description):
        self.category_disease_name = category_disease_name
        self.category_disease_description = category_disease_description