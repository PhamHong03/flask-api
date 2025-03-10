from .type_disease import Type_Disease, db

class Disease(db.Model):
    __tablename__ = 'disease'   
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)