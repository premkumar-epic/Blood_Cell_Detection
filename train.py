import os
from ultralytics import YOLO
import wandb

# Download pre-trained weights
if not os.path.exists("models/yolov10n.pt"):
    print("Downloading yolov10n.pt...")
    os.system(
        "wget -O models/yolov10n.pt [https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt](https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt)"
    )
else:
    print("yolov10n.pt already exists.")

# Weights & Biases setup
wandb_api_key = os.getenv("WANDB_API_KEY")
if wandb_api_key:
    print("Logging into Weights & Biases...")
    wandb.login(key=wandb_api_key)
    use_wandb = True
else:
    print("WANDB_API_KEY not found. Training will proceed without W&B logging.")
    use_wandb = False

# Load model
model = YOLO("models/yolov10n.pt")

# Train the model
model.train(
    data="data/blood-cell-detection-4/data.yaml",
    epochs=25,
    batch=32,
    plots=True,
    project="runs",
    name="detect/train_blood_cells",
)
