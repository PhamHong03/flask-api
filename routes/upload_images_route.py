from flask import Blueprint, request, jsonify   
import os

upload_images_bp = Blueprint('upload_images_bp', __name__)

@upload_images_bp.route('/upload_images', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({"message": "No file part"}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    if file:
        file_path = os.path.join(upload_images_bp.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200
