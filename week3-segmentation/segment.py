from ultralytics import YOLO
import os

model = YOLO("yolov8n-seg.pt")   # segmentation model

input_folder = "images"

for img in os.listdir(input_folder):
    path = os.path.join(input_folder, img)
    print(f"Segmenting: {path}")
    model(path, save=True)
