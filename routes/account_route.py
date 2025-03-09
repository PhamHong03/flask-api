from flask import Blueprint, request, jsonify
from controllers.account_controller import  get_all_accounts, register_account
from firebase_admin import auth
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

@account_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        id_token = data.get('idToken')  

        decoded_token = auth.verify_id_token(id_token)  
        user_id = decoded_token['uid']

        return jsonify({'message': 'Đăng nhập thành công', 'uid': user_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 401


@account_bp.route('/sendFirebaseToken', methods=['POST'])
def send_firebase_token():
    data = request.get_json()
    id_token = data.get("idToken")
    if not id_token:
        return jsonify({"error": "Missing idToken"}), 400
    return jsonify({"message": "Token received!", "idToken": id_token}), 200

@account_bp.route("/accounts", methods=["GET"])
def get_accounts():
    return get_all_accounts()
