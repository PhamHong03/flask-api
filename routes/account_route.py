from flask import Blueprint, request, jsonify
from controllers.account_controller import  get_all_accounts, register_account

account_bp = Blueprint("account", __name__)

@account_bp.route("/register",methods=["POST"])
def register():
    data = request.get_json()
    print(data)
    auth_header = request.headers.get("Authorization")
    print(f"Authorization Token: {auth_header}")  

    if not data:
        return jsonify({"message": "Dữ liệu không hợp lệ"}), 400

    if not auth_header:
        return jsonify({"message": "Authorization header missing"}), 401

    return register_account(data, auth_header)

@account_bp.route("/accounts", methods=["GET"])
def get_accounts():
    return get_all_accounts()
