import tensorflow as tf
from tensorflow.keras.models import load_model


import numpy as np
from tensorflow.keras.preprocessing import image
import cv2
import matplotlib.pyplot as plt


model_path = "./models/liver-histopathology-fibrosis-ultrasound-model.keras"


model = load_model(model_path)
print("\n✅ Model loaded successfully!")


def prediction_liver(test_img_path):
    test_img = image.load_img(test_img_path, target_size=(224, 224))
    img_array = image.img_to_array(test_img) / 255.0
    img_array = np.expand_dims(img_array, axis=0) 
    prediction = model.predict(img_array)
    if prediction.shape[1] == 1:  # Phân loại nhị phân
        predicted_label = "Có bệnh" if prediction[0][0] > 0.5 else "Không có bệnh"
    else: 
        predicted_label = np.argmax(prediction)

    return predicted_label

image_path = "./data/a107.jpg"

model = load_model(model_path)

if model:
    print("\n🔍 Đang dự đoán ảnh...\n")
    result = prediction_liver(image_path)
    print(result)
