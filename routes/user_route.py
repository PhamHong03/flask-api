

from flask import Blueprint, request, jsonify
from controllers.user_controller import UserController
from models.user import User
from database import db
import jwt


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({"message": "Không được bỏ trống"}), 400
        
        new_user = User(username=username, email=email, password=password)  
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Đăng ký thành công"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@user_bp.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "Không được bỏ trống"}), 400
        
        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hasd(user.password, password):
            return jsonify({"message": "Sai tài khoản hoặc mật khẩu"}), 401 

        token = jwt

    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

@user_bp.route('/user', methods=["GET"])
def get_user():
    users = UserController.get_all_user()
    return jsonify([{"id": user.id, "name": user.name, "email": user.email} for user in users]) 

@user_bp.route('/user/<int:user_id>', methods=["GET"])
def get_user_by_id(user_id):    
    user = UserController.get_user_by_id(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email})
