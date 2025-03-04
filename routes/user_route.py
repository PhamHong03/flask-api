

from flask import Blueprint, request, jsonify
from controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user', methods=["GET"])
def get_user():
    users = UserController.get_all_user()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users]) 

@user_bp.route('/user/<int:user_id>', methods=["GET"])
def get_user_by_id(user_id):    
    user = UserController.get_user_by_id(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email})
