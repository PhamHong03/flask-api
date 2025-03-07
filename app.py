from flask import Flask, jsonify, request
from flask_migrate import Migrate 
from config.config import Config
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from database import db

from models import Account, Specialization, Education
from routes.specialization_route import specialization_bp
from routes.education_route import education_bp
from routes.account_route import account_bp

import pyrebase
import json

# from routes.doctor_route import doctor_bp
import os
from dotenv import load_dotenv


load_dotenv()
print(os.getenv("SECRET_KEY"))

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
bcrypt = Bcrypt(app)
# # Cấu hình kết nối MySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'healthy_and_diagnosis'

# Cấu hình kết nối MySQL với SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/healthy_and_diagnosis'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Khởi tạo MySQL
# mysql = MySQL(app)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


app.register_blueprint(specialization_bp)
app.register_blueprint(education_bp)
app.register_blueprint(account_bp)
# app.register_blueprint(doctor_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
