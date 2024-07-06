#pip install opencv-python-headless
#pip install serial
#pip install mediapipe
#pip install numpy

import cv2
import numpy as np
import serial
import mediapipe as mp

# Initialize serial connection with Arduino Ide
arduino = serial.Serial('COM32', 9600)

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

def detect_sign(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Define templates for signs
    up_template = cv2.imread('up.jpg', cv2.IMREAD_GRAYSCALE)
    down_template = cv2.imread('down.jpg', cv2.IMREAD_GRAYSCALE)
    right_template = cv2.imread('right.jpg', cv2.IMREAD_GRAYSCALE)
    left_template = cv2.imread('left.jpg', cv2.IMREAD_GRAYSCALE)
    stop_template = cv2.imread('stop.jpg', cv2.IMREAD_GRAYSCALE)
    
        # Resize templates
    template_size = (50, 50)  # Adjust size as needed
    up_template = cv2.resize(up_template, template_size)
    down_template = cv2.resize(down_template, template_size)
    right_template = cv2.resize(right_template, template_size)
    left_template = cv2.resize(left_template, template_size)
    stop_template = cv2.resize(stop_template, template_size)
    
    
    # Perform template matching
    try:
        res_up = cv2.matchTemplate(gray, up_template, cv2.TM_CCOEFF_NORMED)
        res_down = cv2.matchTemplate(gray, down_template, cv2.TM_CCOEFF_NORMED)
        res_right = cv2.matchTemplate(gray, right_template, cv2.TM_CCOEFF_NORMED)
        res_left = cv2.matchTemplate(gray, left_template, cv2.TM_CCOEFF_NORMED)
        res_stop = cv2.matchTemplate(gray, stop_template, cv2.TM_CCOEFF_NORMED)
    except cv2.error as e:
        print("Error:", e)
        return None
    
    threshold = 0.8
     
    # Check if any sign is detected
    if np.max(res_up) > threshold:
        return 'forward'
    elif np.max(res_down) > threshold:
        return 'backward'
    elif np.max(res_right) > threshold:
        return 'right'
    elif np.max(res_left) > threshold:
        return 'left'
    elif np.max(res_stop) > threshold:
        return 'stop'
    else:
        return None

def send_command(command):
    arduino.write(command.encode())  # Send command to Arduino

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
                return "stop"  # Closed hand gesture (fist)
            else:
                if thumb_tip.x < index_tip.x:
                    return "left"
                else:
                    return "right"
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
            cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # Send command to Arduino based on detected gesture
            if gesture == 'left':
                send_command('a\n')  # Left
                print("left detected")
            elif gesture == 'right':
                send_command('d\n')  # Right
                print("right detected")
            elif gesture == 'stop':
                send_command('x\n')  # Stop
                print("stop detected")

        # Detect sign in the frame
        sign = detect_sign(frame)
        # Display the detected sign on frame
        
        if sign is not None:
            cv2.putText(frame, sign, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            # Send command to Arduino based on detected sign
            if sign == 'forward':
                send_command('w\n')  # Forward
                print("forward detected")
            elif sign == 'backward':
                send_command('s\n')  # Backward
                print("backward detected")
            elif sign == 'right':
                print("stop detected")
                send_command('d\n')  # Right
                print("right detected")
            elif sign == 'left':
                send_command('a\n')  # Left
                print("left detected")
            elif sign == 'stop':
                send_command('x\n')  # Stop

        # Display the frame
        cv2.imshow('Frame', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release webcam and close all windows
cap.release()
cv2.destroyAllWindows()
