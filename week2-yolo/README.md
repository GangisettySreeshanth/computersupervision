# Week 2 — YOLO Object Detection & Video Pipeline

## 📌 Objective

Apply object detection using a pretrained YOLOv8 model and extend it to a full pipeline:

* Detect objects in multiple images
* Generate annotated outputs
* Convert frames into a video
* Add background audio

---

## ⚙️ Environment Setup

* Python (venv)
* Ultralytics YOLO

```bash
pip install -U ultralytics
```

---

## 🚀 Implementation

### 1. Single Image Detection

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model("bus.jpg", save=True)
```

---

### 2. Multiple Image Detection

```python
from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")
input_folder = "images"

for img in os.listdir(input_folder):
    path = os.path.join(input_folder, img)
    model(path, save=True)
```

---

## 📊 Output (Sample)

The model detects:

* Person
* Bus
* Stop sign

### 🔍 Detection Result

![Detection Output](output.jpg)

---

## 🎬 Video Generation Pipeline

### Step 1: Frames → Video

```bash
ffmpeg -framerate 0.5 -i frames/img_%03d.jpg -c:v libx264 -pix_fmt yuv420p video.mp4
```

### Step 2: Add Audio

```bash
ffmpeg -i video.mp4 -i music.mp3 -c:v copy -c:a aac -shortest final_video.mp4
```

---

## 🎥 Final Output

The final video demonstrates:

* Object detection across multiple images
* Smooth frame sequencing
* Audio integration

👉 [View Final Video](final_video.mp4)

---

## 🔄 Pipeline Overview

Images → YOLO Detection → Annotated Frames → Video → Audio Integration

---

## ⚠️ Limitation

Detection is limited to object classes present in the pretrained YOLOv8 model.

---

## 📁 Folder Structure

```
week2-yolo
├── detect.py
├── multi_detect.py
├── output.jpg
├── final_video.mp4
└── README.md
```

---

## ✅ Conclusion

Successfully implemented an end-to-end computer vision pipeline using YOLOv8, extending from single-image detection to multi-image video generation with audio.

---

