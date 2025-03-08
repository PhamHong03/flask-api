import firebase_admin
from firebase_admin import credentials, auth

#Load Firebase Admin SDK
cred = credentials.Certificate("healthyanddiagnose-firebase.json")
firebase_admin.initialize_app(cred)


def verify_firebase_token(auth_header):
    if not auth_header:
        return None, {"message":"Token không được cung cấp"}, 401

    id_token = auth_header.split("Bearer ")[-1]
    print(f"Received Token: {id_token}") 
    
    try:
        decode_token = auth.verify_id_token(id_token)
        firebase_uid = decode_token.get("uid")
        return firebase_uid, None, 200
    except Exception as e:
        print(f"Token error: {str(e)}")  
        return None, {"message": "Token không hợp lệ"}, 401
