from flask_mysqldb import MySQL
from flask import jsonify

mysql = MySQL()
class Doctor:
    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("""
            SELECT VC_MA, VC_HO_TEN, VC_GIOI_TINH, VC_DIA_CHI, VC_SDT, VC_EMAIL, CK_TEN, TDHV_TEN
            FROM vienchuc
            JOIN chuyenkhoa ON vienchuc.CK_MA = chuyenkhoa.CK_MA
            JOIN trinhdohocvan ON vienchuc.TDHV_MA = trinhdohocvan.TDHV_MA
        """)
        result = cur.fetchall()
        cur.close()
        return [
            {
                "id": row[0],
                "name_Doctor": row[1],
                "gender_Doctor": row[2],
                "address_Doctor": row[3],
                "phone_Doctor": row[4],
                "email_Doctor": row[5],
                "specialization_Doctor": row[6],
                "education_Doctor": row[7]
            } for row in result
        ]