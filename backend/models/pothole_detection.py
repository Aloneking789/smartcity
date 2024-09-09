from ultralytics import YOLO

# Load YOLO model
model = YOLO('backend\models\yolov8_pothole_model.pt')  # Pre-trained or fine-tuned model

def detect_pothole(frame):
    # Apply YOLOv8 to the frame
    results = model(frame)
    
    # Check if pothole is detected in the results
    for result in results:
        if result['class'] == 'pothole':  # Assuming pothole class exists
            return True
    return False
