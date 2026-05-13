from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Train model
model.train(
    data="dataset.yaml",
    epochs=50,
    imgsz=384
)
