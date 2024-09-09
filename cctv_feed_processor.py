import cv2
from ultralytics import YOLO
from backend.models.pothole_detection import detect_pothole
# from backend.models.weapon_detection import detect_weapon
from backend.utils.speed_detection import calculate_speed
from backend.utils.alerting import send_alert

# Access CCTV feed
cap = cv2.VideoCapture("rtsp://184.72.239.149/vod/mp4:BigBuckBunny_115k.mov")

while True:
    ret, frame = cap.read()
    if ret:
        # Apply detection models
        pothole_detected = detect_pothole(frame)
        # weapon_detected = detect_weapon(frame)

        if pothole_detected:
            send_alert("Pothole detected at XYZ location", "+911234567890")
        
        # if weapon_detected:
            # send_alert("Weapon detected at XYZ location", "+911234567890")
        
        # Optionally display processed frame
        cv2.imshow('CCTV Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
