import pyrebase
from flask import request, jsonify
import jwt
from app import db
from models import Account
from controllers.account_controller import verify_firebase_token


def register_account(data, auth_header):
    firebase_uid, error, status_code = verify_firebase_token(auth_header)
    if error:
        return jsonify(error) , status_code
    
    if Account.query.filter_by(email=data["email"]).first():
        return {"message": "Email đã được sử dụng"}, 400
    new_account = Account(
        firebase_uid=firebase_uid,
        username=data['username'],
        email=data['email'],
        password=data['password'],
        phone_number = data['phone_number'],
        role=data['role']
    )
    db.session.add(new_account)
    db.session.commit()

    return {"message": "Tạo tài khoản thành công"}, 200