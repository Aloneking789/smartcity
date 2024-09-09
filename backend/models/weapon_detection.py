# from ultralytics import YOLO

# # Load YOLO model for weapon detection
# model = YOLO('yolov8_weapon_model.pt')

# def detect_weapon(frame):
#     # Apply YOLOv8 to the frame
#     results = model(frame)
    
#     # Check if a weapon is detected in the results
#     for result in results:
#         if result['class'] == 'weapon':  # Assuming weapon class exists
#             return True
#     return False
