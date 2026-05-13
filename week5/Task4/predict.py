from ultralytics import YOLO

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Run prediction
results = model.predict(
    source="images",
    conf=0.1,      # VERY IMPORTANT (lower threshold)
    save=True,
    show=True
)
