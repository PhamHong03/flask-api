from flask import Flask, jsonify, request, render_template
from flask_migrate import Migrate 
from config.config import Config
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from models import Account, Specialization, Education, Category_Disease, Diagnose_Disease, Physician, Patient, Room, MedicalHistory, ApplicationForm
from routes.specialization_route import specialization_bp
from routes.education_route import education_bp
from routes.account_route import account_bp
from routes.category_disease_route import category_disease_bp
from routes.diagnose_disease_route import diagnose_disease_bp
from routes.physician_route import physician_bp
from routes.patient_route import patient_bp 
from routes.room_route import room_bp
from routes.medical_history_route import medical_history_bp
from routes.application_form_route import application_form_bp
from database import db
import pyrebase
import json
import os
from dotenv import load_dotenv
from datetime import datetime, timezone
import pytz

# Kiểm tra giờ UTC
utc_now = datetime.now(pytz.utc)
# print(f"🕰 Server Time (UTC): {utc_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

# Kiểm tra giờ Việt Nam
vn_tz = pytz.timezone('Asia/Ho_Chi_Minh')
vn_now = datetime.now(vn_tz)
# print(f"🇻🇳 Vietnam Time: {vn_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

load_dotenv()
# print(os.getenv("SECRET_KEY"))
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

bcrypt = Bcrypt(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/healthy_and_diagnosis'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(specialization_bp)
app.register_blueprint(education_bp)
app.register_blueprint(account_bp)
app.register_blueprint(category_disease_bp)
app.register_blueprint(diagnose_disease_bp)
app.register_blueprint(physician_bp)
app.register_blueprint(patient_bp)
app.register_blueprint(room_bp)
app.register_blueprint(medical_history_bp)
app.register_blueprint(application_form_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
