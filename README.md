# Blood Cell Detection using YOLOv10

## Overview

This project implements a blood cell detection system using the state-of-the-art YOLOv10 object detection model. It's trained on a custom dataset from Roboflow to identify various blood cell types (e.g., Red Blood Cells, White Blood Cells, Platelets). The project provides scripts for training, prediction, and an interactive web interface for real-time inference.

## Features

- 🔍 YOLOv10 Model: Efficient and powerful for accurate object detection.
- 📦 Custom Dataset Integration: Easily connect with Roboflow for dataset management.
- 🏋️ Training Script: train.py to fine-tune the YOLOv10 model.
- 📸 Prediction Script: predict.py to infer on new images or directories.
- 🌐 Gradio Web App: app.py offers a real-time interactive detection interface.
- 📊 Weights & Biases (Optional): Log metrics and training visualizations.

## Project Structure

```
Blood-Cell-Detection-YOLOv10/
├── .gitignore                       # Files/folders to ignore in Git
├── README.md                        # This file - project overview and instructions
├── requirements.txt                 # Python dependencies
├── train.py                         # Script to train the YOLOv10 model
├── predict.py                       # Script to run inference on images/directories
├── app.py                           # Gradio web application for real-time detection
├── data/
│   └── blood-cell-detection-4/
│       ├── data.yaml                # Dataset configuration
│       ├── train/                   # Training images and labels
│       ├── val/                     # Validation images and labels
│       └── test/                    # Test images and labels
├── models/
│   ├── yolov10n.pt                  # Pre-trained YOLOv10 nano weights
│   └── best.pt                      # Trained model weights (generated after training)
└── notebooks/
    └── blood_cell_detection_colab.ipynb  # Colab notebook for development
```

## Setup and Installation

1. 🚀 Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Blood-Cell-Detection-YOLOv10.git
cd Blood-Cell-Detection-YOLOv10
```

(Replace YOUR_USERNAME with your actual GitHub username.)

2. 🧪 Create a virtual environment (recommended):

```bash
python -m venv venv
```

Activate the environment:

- On Linux/macOS:

```bash
source venv/bin/activate
```

- On Windows CMD:

```bash
.env\Scriptsctivate
```

- On Windows PowerShell:

```bash
.env\Scripts\Activate.ps1
```

3. 📦 Install dependencies:

```bash
pip install -r requirements.txt
```

4. ⬇️ Download pre-trained YOLOv10 weights:

```bash
mkdir -p models
wget -O models/yolov10n.pt https://github.com/jameslahm/yolov10/releases/download/v1.0/yolov10n.pt
```

(If wget is unavailable, manually download from the URL above and place it in models/.)

5. 🧬 Download your Roboflow dataset:

- Set your Roboflow API key as an environment variable:

Linux/macOS:

```bash
export ROBOFLOW_API_KEY="YOUR_ROBOFLOW_API_KEY"
```

Windows CMD:

```bash
set ROBOFLOW_API_KEY="YOUR_ROBOFLOW_API_KEY"
```

Windows PowerShell:

```powershell
$env:ROBOFLOW_API_KEY="YOUR_ROBOFLOW_API_KEY"
```

- Run the dataset download script:

```bash
python -c "from roboflow import Roboflow; import os; rf = Roboflow(api_key=os.environ.get('ROBOFLOW_API_KEY')); project = rf.workspace('clg-vtj9f').project('blood-cell-detection-bsbvn'); version = project.version(4); version.download('yolov9', location='data/'); print('Dataset downloaded successfully to the data/ folder.')"
```

Your dataset will appear in: data/blood-cell-detection-4/


> 💡 **Tip:** If your PC has low specifications, you can copy-paste the contents of `notebooks/training_experiments.ipynb` into [Google Colab](https://colab.research.google.com/), then go to **Runtime > Change runtime type**, and set:
> - **Hardware accelerator:** GPU (preferably T4)
> - **Runtime type:** Python
> This will give you much faster training and inference performance.


## Usage

### 1. 🏋️‍♀️ Train the Model

```bash
python train.py
```

Trained weights (best.pt) will be saved in:

runs/detect/train_blood_cells/weights/

### 2. 🔍 Run Predictions

```bash
python predict.py --weights runs/detect/train_blood_cells/weights/best.pt --source data/blood-cell-detection-4/test/images --name blood_cell_predictions
```

Annotated results will appear in:

runs/detect/blood_cell_predictions/

### 3. 🌐 Launch the Web App (Gradio)

```bash
python app.py
```

Visit the local URL (e.g., http://127.0.0.1:7860/) in your browser to upload images and view detections.

## Acknowledgements

- YOLOv10 - Ultralytics
- Roboflow - Dataset annotation and download
- Gradio - UI for real-time inference

## License

This project is open-source under the MIT License. Create a LICENSE file and paste the MIT license text if distributing publicly.
