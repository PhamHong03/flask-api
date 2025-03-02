from flask import Blueprint, jsonify
from models.education import Education

education_bp = Blueprint("education", __name__)

@education_bp.route("/trinhdohocvan", methods=["GET"])
def get_trinh_do_hoc_van():
    return jsonify(Education.get_all())
