# Week 3 — Semantic Segmentation & Video Comparison

## 📌 Objective

Extend object detection to **semantic segmentation** and create a complete visual pipeline:

* Segment multiple images
* Convert segmented outputs into video
* Compare Raw vs Detection vs Segmentation using stacked video
* Add audio for final presentation

---

## 🧠 Concept Overview

### 🔹 Object Detection

* Detects objects using **bounding boxes**
* Example: person, bus, stop sign

### 🔹 Semantic Segmentation

* Classifies **each pixel**
* Highlights object regions with **colored masks**
* Provides deeper understanding than detection

---

## ⚙️ Model Used

```bash
yolov8n-seg.pt
```

* Pretrained YOLOv8 segmentation model
* Trained on COCO dataset
* Supports multiple object classes

---

## 🚀 Implementation

### 🔹 Multi-Image Segmentation

```python
from ultralytics import YOLO
import os

model = YOLO("yolov8n-seg.pt")

input_folder = "images"

for img in os.listdir(input_folder):
    path = os.path.join(input_folder, img)
    model(path, save=True)
```

---

## 📊 Output Description

* Each object is assigned:

  * A **mask color**
  * A **class label**
* Transparent overlays highlight object regions

---

## 🎬 Video Generation Pipeline

### Step 1: Raw Video

```bash
ffmpeg -framerate 0.5 -i images/img_%03d.jpg -c:v libx264 -pix_fmt yuv420p raw_video.mp4
```

### Step 2: Detection Video (Week 2)

Generated using YOLO object detection

---

### Step 3: Segmentation Video

```bash
ffmpeg -framerate 0.5 -i seg_frames/img_%03d.jpg -c:v libx264 -pix_fmt yuv420p seg_video.mp4
```

---

## 🔄 Final Comparison (Key Output)

Three videos are stacked vertically:

* Top → Raw input
* Middle → Object detection
* Bottom → Semantic segmentation

### 🔹 Stacking Command

```bash
ffmpeg -i raw_fixed.mp4 -i detect_fixed.mp4 -i seg_fixed.mp4 -filter_complex "vstack=inputs=3" -an stacked_video.mp4
```

---

## 🎵 Audio Integration

```bash
ffmpeg -i stacked_video.mp4 -i music.mp3 -c:v copy -c:a aac -shortest final_stack_video.mp4
```

---

## 🎥 Final Output

👉 **Stacked Comparison Video:**
`final_stack_video.mp4`

This video clearly demonstrates the progression:

* Raw data → Detection → Segmentation

---

## 📈 Performance Metrics

Since a pretrained model is used:

* Metrics such as **Precision, Recall, mAP** are predefined
* No custom training was performed

Typical meaning:

* **Precision** → correctness of detections
* **Recall** → completeness of detections
* **mAP** → overall performance

---

## 🔄 Pipeline Summary

Images → Segmentation → Frames → Video → Stack → Audio

---

## ⚠️ Limitations

* Only detects classes trained in YOLOv8
* No custom dataset training
* Performance depends on pretrained model

---

## ✅ Conclusion

Successfully implemented semantic segmentation using YOLOv8 and built a complete multimedia pipeline to visualize and compare model outputs.

---

