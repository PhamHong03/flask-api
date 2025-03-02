from flask import Blueprint, jsonify
from models.doctor import Doctor

doctor_bp = Blueprint("doctor", __name__)

@doctor_bp.route("/vienchuc", methods=["GET"])
def get_vien_chuc():
    return jsonify(Doctor.get_all())
