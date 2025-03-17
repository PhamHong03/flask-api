from database import db

class Room(db.Model):
    __tablename = ('room')
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    

    def __init__(self, name):
        self.name = name