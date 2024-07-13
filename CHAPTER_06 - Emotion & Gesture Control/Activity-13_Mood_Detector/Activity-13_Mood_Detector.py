#Pip install opencv-python
#Pip install pyserial

import cv2
import serial

# Initialize serial connection with Arduino
arduino_ide = serial.Serial('com69', 9600)

# Load pre-trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load pre-trained Haar cascade classifier for smile detection
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)

def detect_emotion(gray, faces):
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]  # Region of interest (face) in grayscale

        # Detect smile
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
        for (sx, sy, sw, sh) in smiles:
            return 'smile'

    return 'neutral'

def control_led(emotion):
    if emotion == 'smile':
        arduino_ide.write(b'1')  # Send '1' to Arduino ide to turn on the LED
        print("LED turned ON")
        
    elif emotion == 'neutral':
        arduino_ide.write(b'0')  # Send '0' to Arduino ide to turn off the LED
        print("LED turned OFF")
        

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Detect emotion and control LED
    emotion = detect_emotion(gray, faces)
    control_led(emotion)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()


