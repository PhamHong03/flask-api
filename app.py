from flask import Flask, jsonify, request
from flask_migrate import Migrate 
from config.config import Config
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from models import Account, Specialization, Education
from routes.specialization_route import specialization_bp
from routes.education_route import education_bp
from routes.account_route import account_bp
from database import db
import pyrebase
import json
import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("SECRET_KEY"))
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
