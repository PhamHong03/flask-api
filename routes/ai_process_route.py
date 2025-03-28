from flask import Blueprint, request, jsonify
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

ai_process_bp = Blueprint('ai_process_bp', __name__)

MODEL_PATH = "a./models/liver-histopathology-fibrosis-ultrasound-model.keras" 
model = load_model(MODEL_PATH)  

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))  
    img = img / 255.0 
    img = np.expand_dims(img, axis=0)
    return img

@ai_process_bp.route('/process_image', methods=['POST'])
def process_image():
    data = request.get_json()
    image_path = data.get("file_path")

    if not image_path or not os.path.exists(image_path):
        return jsonify({"message": "File không tồn tại!"}), 400

    img = preprocess_image(image_path)
    prediction = model.predict(img)
    result = np.argmax(prediction) 

    return jsonify({"message": "Xử lý thành công!", "result": int(result)}), 200
