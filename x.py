import cv2
import time

def capture_with_timeout(stream_url, timeout=60):
    cap = cv2.VideoCapture(stream_url)
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('CCTV Feed', frame)
            # Reset the timer if we successfully capture a frame
            start_time = time.time()
        else:
            print("Failed to capture frame, retrying...")
        
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Use your stream URL (replace '0' with stream URL if it's a camera)
stream_url = "rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa"
capture_with_timeout(stream_url, timeout=60)
