from flask import Flask
from flask_mysqldb import MySQL
from database import db

app = Flask(__name__)
app.config.from_object("config.Config")


# Cấu hình kết nối MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'healthy_and_diagnosis'

db.init_app(app)

# Khởi tạo MySQL
mysql = MySQL(app)


@app.route("/")
def hello_world():
    return ""