from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

import cv2

def get_webcam_frame():
    # Get the webcam capture device.
    cap = cv2.VideoCapture(0)
    
    # Check if the webcam is opened successfully.
    if not cap.isOpened():
        print("Could not open webcam.")
        return None
    
    # Capture a frame from the webcam.
    ret, frame = cap.read()
    
    # Check if the frame is captured successfully.
    if not ret:
        print("Could not capture frame from webcam.")
        return None
    
    # Return the frame.
    return frame

# Get the webcam frame.
frame = get_webcam_frame()

# Display the webcam frame.
cv2.imshow("Webcam Frame", frame)

# Wait for a key press.
cv2.waitKey(0)