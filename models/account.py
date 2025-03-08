from database import db
from flask_bcrypt  import  Bcrypt
bcrypt = Bcrypt()
class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100),nullable=False)
    role = db.Column(db.String(100), nullable=False)
    firebase_uid = db.Column(db.String(255), nullable=False, unique=True)

    def __init__(self, firebase_uid, username, email, phone_number, password, role):
        self.firebase_uid = firebase_uid
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.password = self.hash_password(password)  
        self.role = role

    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")
    
    @staticmethod
    def check_password(stored_password, input_password):
        return bcrypt.check_password_hash(stored_password, input_password)