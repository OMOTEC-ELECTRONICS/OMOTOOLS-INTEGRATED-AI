#Pip install serial
#pip install numpy



import cv2
import numpy as np
import serial
import mediapipe as mp

# Initialize serial connection with Arduino
arduino = serial.Serial('COM69', 9600, timeout=1)

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Function to detect hand gestures
def detect_gesture(frame):
    # Convert the image to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe hands
    results = hands.process(frame_rgb)

    # Check if hand landmarks are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the coordinates of the thumb and index finger tips
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Calculate the distance between the thumb and index finger tips
            distance = ((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)**0.5

            # If the distance is small, the hand is closed (fist)
            if distance < 0.05:
                return "Boom"  # Closed hand gesture (fist)
            else:
                return "Hi"  # Open hand gesture
    return None

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        # Detect gesture
        gesture = detect_gesture(frame)

        # Display the gesture on frame
        if gesture is not None:
            cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),2)

            # Send gesture to Arduino via serial
            arduino.write(gesture.encode())

            # Turn on LED if "Hi" is detected
            if gesture == "Hi":
                arduino.write(b'H')

        # Display the frame
        cv2.imshow('Frame', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release webcam and close all windows
cap.release()
cv2.destroyAllWindows()
