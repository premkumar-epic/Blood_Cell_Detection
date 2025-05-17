import gradio as gr
import cv2
import numpy as np
from collections import Counter
from ultralytics import YOLO
import os

# Load the trained model
MODEL_PATH = "runs/detect/train_blood_cells/weights/best.pt"
if not os.path.exists(MODEL_PATH):
    print(f"Error: Model weights not found at {MODEL_PATH}.")
    print("Attempting to load pre-trained yolov10n.pt instead.")
    if not os.path.exists("models/yolov10n.pt"):
        os.system(
            "wget -O models/yolov10n.pt [https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt](https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt)"
        )
    model = YOLO("models/yolov10n.pt")  # Fallback to pretrained
else:
    model = YOLO(MODEL_PATH)

def predict_image(image):
    if image is None:
        return None, "No image uploaded."

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = model(image_rgb, imgsz=640, conf=0.25, verbose=False)
    result = results[0]
    annotated_img = result.plot()
    detections = result.boxes.data

    if detections.numel() == 0:
        detection_str = "No blood cells detected."
    else:
        class_ids = detections[:, 5].cpu().numpy().astype(int)
        class_names = [model.names[int(cls_id)] for cls_id in class_ids]
        count = Counter(class_names)
        detection_str = ", ".join([f"{name}: {count}" for name, count in count.items()])

    return annotated_img, detection_str

app = gr.Interface(
    predict_image,
    inputs=gr.Image(type="numpy", label="Upload an Image"),
    outputs=[
        gr.Image(type="numpy", label="Annotated Image"),
        gr.Textbox(label="Detection Count"),
    ],
    title="Blood Cell Detection & Count",
    description="Upload a microscope image to detect blood cells.",
)

if __name__ == "__main__":
    app.launch(debug=True)
