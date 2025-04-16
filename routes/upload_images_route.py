from flask import Blueprint, request, jsonify
import os
import uuid
from werkzeug.utils import secure_filename
from datetime import datetime
from AI import predict_liver_disease
from database import db
from models.images import Images

upload_images_bp = Blueprint('upload_images_bp', __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_images_bp.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"message": "Không có file!"}), 400

    file = request.files['file']
    physician_id = request.form.get("physician_id")
    appointment_id = request.form.get("appointment_id")
    print(f"appointment_id: {appointment_id}")
    print(f"physician_id: {physician_id}, file: {file}")
    if not physician_id or not appointment_id:
        return jsonify({"message": "Thiếu thông tin bác sĩ hoặc mã phiếu khám!"}), 400

    if file.filename == '':
        return jsonify({"message": "Không có file được chọn!"}), 400

    if not allowed_file(file.filename):
        return jsonify({"message": "Định dạng file không hợp lệ!"}), 400

    ext = file.filename.rsplit('.', 1)[1].lower()
    filename = f"{physician_id}_{appointment_id}_{uuid.uuid4().hex}.{ext}"
    file_path = os.path.join(UPLOAD_FOLDER, secure_filename(filename))
    file.save(file_path)

    result = predict_liver_disease(file_path)
    print(f"Raw result: {result}")


    if isinstance(result, int):
        match result:
            case 0:
                disease_id = 1
                diagnosis_text = "Không có bệnh"
            case 1:
                disease_id = 2
                diagnosis_text = "Có bệnh giai đoạn 1"
            case 2:
                disease_id = 3
                diagnosis_text = "Có bệnh giai đoạn 2"
            case 3:
                disease_id = 4
                diagnosis_text = "Có bệnh giai đoạn 3"
            case 4:
                disease_id = 5
                diagnosis_text = "Có bệnh giai đoạn 4"
            case _:
                disease_id = 1
                diagnosis_text = "Kết quả không hợp lệ"
    
    else:

        disease_id = 1
        diagnosis_text = "Kết quả không hợp lệ"

    print(f"disease_id: {disease_id}")
    print(f"diagnosis_text: {diagnosis_text}")


    existing_image = Images.query.filter_by(physician_id=physician_id, appointment_form_id=appointment_id).first()

    if existing_image:
        existing_image.diagnose_disease_id = disease_id
        existing_image.images_path = file_path
    else:
        new_image = Images(
            images_path=file_path,
            physician_id=int(physician_id),
            appointment_form_id=int(appointment_id),
            diagnose_disease_id=disease_id
        )
        db.session.add(new_image)

    db.session.commit()

    return jsonify({
        "appointment_id": appointment_id,
        "physician_id": physician_id,
        "message": "Tải lên thành công!",
        "images_path": file_path,
        "diagnosis": diagnosis_text,
        "images_created": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "diseases_id": disease_id
    }), 200
