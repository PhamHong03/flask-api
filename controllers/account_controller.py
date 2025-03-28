from flask import jsonify, request
from database import db
from models.account import Account
from controllers.auth_controller import verify_firebase_token   

def register_account(data, auth_header): 
    firebase_uid, error, status_code = verify_firebase_token(auth_header)
    print(f"Firebase UID: {firebase_uid}")
    if error:
        return jsonify(error), status_code
    
    if Account.query.filter_by(email=data["email"]).first():
        return jsonify({"message": "Email đã được sử dụng"}), 400

    hashed_password = Account.hash_password(data['password'])

    new_account = Account(
        firebase_uid=firebase_uid,
        email=data['email'],
        password=hashed_password,  
        role=data['role']
    )

    db.session.add(new_account)
    db.session.commit()
    print("Insert successfully")

    return jsonify({
        "message": "Tạo tài khoản thành công",
        "id": new_account.id, 
        "email": new_account.email,
        "role": new_account.role
    }), 201

def login_account():
    auth_header = request.headers.get("Authorization")
    firebase_uid, error, status_code = verify_firebase_token(auth_header)

    if error:
        return jsonify(error), status_code
    account = Account.query.filter_by(firebase_uid=firebase_uid).first()

    if not account:
        return jsonify({"message": "Tài khoản không tồn tại"}), 404
    
    return jsonify({
        "message": "Đăng nhập thành công",
        "account": {
            "id": account.id,
            "email": account.email,
            "role" : account.role
        }
        }), 200

def get_all_accounts():
    """Lấy danh sách tất cả tài khoản"""
    accounts = Account.query.all()
    return jsonify([{
        "id": acc.id,
        "firebase_uid": acc.firebase_uid,
        "email": acc.email,
        "role": acc.role
    } for acc in accounts]), 200
