
from models.user import User    
from database import db

class UserController:

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def get_all_user():
        return User.query.all()