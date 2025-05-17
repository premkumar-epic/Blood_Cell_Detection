import argparse
from ultralytics import YOLO
import os

def main():
    parser = argparse.ArgumentParser(description="Run YOLOv10 prediction on images.")
    parser.add_argument(
        "--weights",
        type=str,
        required=True,
        help="Path to the trained model weights.",
    )
    parser.add_argument(
        "--source",
        type=str,
        required=True,
        help="Path to the image(s) or directory.",
    )
    parser.add_argument(
        "--conf", type=float, default=0.25, help="Confidence threshold."
    )
    parser.add_argument(
        "--imgsz", type=int, default=640, help="Image size for inference."
    )
    parser.add_argument(
        "--name",
        type=str,
        default="predict_results",
        help="Name for the prediction run directory.",
    )
    args = parser.parse_args()

    if not os.path.exists(args.weights):
        print(f"Error: Model weights not found at {args.weights}")
        return

    model = YOLO(args.weights)
    results = model.predict(
        source=args.source,
        conf=args.conf,
        imgsz=args.imgsz,
        project="runs",
        name=args.name,
    )

    print(f"Predictions saved to runs/detect/{args.name}")

if __name__ == "__main__":
    main()
