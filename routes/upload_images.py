# from flask import Blueprint, request, jsonify
# from datetime import datetime
# import os

# upload_images_bp = Blueprint('upload_images_bp', __name__)

# @upload_images_bp.route('/upload_images', methods=['POST'])
# def upload_images():
#     try:
        
#         patient_id = request.form.get(patient_id)
#         if not patient_id:
#             return jsonify({"message": "Yêu cầu nhập mã bệnh nhân"}), 400  
        

#         if 'image' not in request.files:
#             return jsonify({"message": "Không tìm thấy hình ảnh"}), 400 
        
#         image_file = request.files['image']

#         exam_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#         filename = f"{patient_id}_{exam_date}.jpg"

#         filepath = os.path.join('UPLOAD_FOLDER', filename)

#         image_file.save(filepath)

#         return jsonify({"message": "Chọn ảnh thành công!"}), 200
    
#     except Exception as e:
#         return jsonify({"message": str(e)}), 500
    