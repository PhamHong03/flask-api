from flask import Blueprint, request, jsonify
from controllers.education_controller import EducationController

education_bp = Blueprint('education_bp', __name__)

@education_bp.route('/education', methods=['GET'])
def get_all_education():
    educations = EducationController.get_all_education()

    return jsonify([{"id": e.id, "name": e.name} for e in educations])


@education_bp.route('/educations/<int:education_id>', methods=['GET'])
def get_education_by_id(education_id):
    educ = EducationController.get_education_by_id(education_id)

    if educ:
        return jsonify({"id": educ.id, "name": educ.name})

    return jsonify({"message": "Education not found"}), 404

@education_bp.route('/education', methods=["POST"])
def create_education():
    data = request.json
    education = EducationController.create_education(data)
    return jsonify({"message": "Education created", "id": education.id}), 201


@education_bp.route('/educations/<int:education_id>', methods=['PUT'])
def update_education(education_id):
    data = request.json
    education = EducationController.update_education(education_id, data)

    if education:
        return jsonify({"message": "Education updated"})
    
    return jsonify({"message":"Education not found"}), 404

@education_bp.route('/education_id', methods=['DELETE'])
def delete_education(education_id):
    education = EducationController.delete_education(education_id)

    if education:
        return jsonify({"message":"Education deleted"})
    
    return jsonify({"message": "Education not found"}), 405