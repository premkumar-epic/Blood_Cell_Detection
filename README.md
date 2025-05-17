
# Blood Cell Detection using YOLOv10

A project for detecting and counting blood cells from microscope images using YOLOv10.

## 🚀 Features

- YOLOv10 model training using custom dataset from Roboflow
- Inference and visualization
- Gradio web UI for real-time prediction

## 🛠️ Installation

```bash
git clone https://github.com/yourusername/blood-cell-detection.git
cd blood-cell-detection
pip install -r requirements.txt
```

## 📦 Setup

1. Download `yolov10n.pt` and place it in `models/`
2. Download your Roboflow dataset (e.g., YOLO format) and extract it into the `data/` folder

## 🏋️‍♂️ Training

```bash
python scripts/train.py
```

## 🔍 Inference

```bash
python scripts/predict.py
```

## 🌐 Gradio App

```bash
python scripts/gradio_app.py
```
