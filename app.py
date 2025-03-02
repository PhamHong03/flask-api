from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS
from models import Doctor, Specialization, Education


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Cấu hình kết nối MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'healthy_and_diagnosis'

# Khởi tạo MySQL
mysql = MySQL(app)

#API lấy danh sách chuyên khoa của bác sĩ
@app.route("/chuyenkhoa", methods=["GET"])
def get_chuyen_khoa():
    return jsonify(Specialization.get_all())


@app.route("/trinhdohocvan", methods=["GET"])
def  get_trinh_do_hoc_van():
    return jsonify(Education.get_all())


@app.route("/vienchuc",methods=["GET"])
def get_vien_chuc():
    return jsonify(Doctor.get_all())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)