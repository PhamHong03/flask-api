from flask_mysqldb import MySQL
from flask import jsonify

mysql = MySQL()

class Specialization:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT CK_MA, CK_TEN FROM trinhdohocvan")
        result = cur.fetchall()
        cur.close()
        return [{"id": row[0], "name_specialization": row[1]} for row in result]