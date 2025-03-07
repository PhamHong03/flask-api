from flask import Blueprint, request
from controllers.account_controller import register_account, get_all_accounts

account_bp = Blueprint("account", __name__)

@account_bp.route("/register",methods=["POST"])
def register():
    data = request.get_json()
    auth_header  = request.headers.get("Authorization")

    if not data:
        return {"message": "Dữ liệu không hợp lệ"}, 400
    
    return register_account(data, auth_header)


@account_bp.route("/accounts", methods=["GET"])
def get_accounts():
    return get_all_accounts()
