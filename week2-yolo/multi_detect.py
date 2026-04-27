from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

input_folder = "images"

for img in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img)
    print(f"Processing: {img_path}")
    model(img_path, save=True)
