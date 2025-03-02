from flask_mysqldb import MySQL
from flask import jsonify

mysql = MySQL()

class Education:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT TDHV_MA, TDHV_TEN FROM trinhdohocvan")
        result  = cur.fetchall()
        cur.close()
        return [{"id": row[0], "name_education": row[1]} for row in result]