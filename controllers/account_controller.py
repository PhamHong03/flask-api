from flask import jsonify
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
        username=data['username'],
        email=data['email'],
        phone_number=data['phone_number'],
        password=hashed_password,  
        role=data['role']
    )

    db.session.add(new_account)
    db.session.commit()
    print("Insert successfully")
    return jsonify({"message": "Tạo tài khoản thành công"}), 201

def get_all_accounts():
    """Lấy danh sách tất cả tài khoản"""
    accounts = Account.query.all()
    return jsonify([{
        "id": acc.id,
        "firebase_uid": acc.firebase_uid,
        "username": acc.username,
        "email": acc.email,
        "phone_number": acc.phone_number,
        "role": acc.role
    } for acc in accounts]), 200
