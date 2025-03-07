import firebase_admin
from firebase_admin import credentials, auth

#Load Firebase Admin SDK
cred = credentials.Certificate("heathyadndiagnoise-firebase.json")
firebase_admin.initialize_app(cred)


