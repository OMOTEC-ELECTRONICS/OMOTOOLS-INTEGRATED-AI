#Pip install open-cv python
#Pip install serial
#pip install numpy

import cv2
import numpy as np
import serial

# Initialize serial connection with Arduino
arduino = serial.Serial('COM3', 9600)

def detect_sign(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define templates for signs
    forward_template = cv2.imread("forward.png", 0)
    backward_template = cv2.imread("backward.png", 0)
    right_template = cv2.imread("right.png", 0)
    left_template = cv2.imread("left.png", 0)
    stop_template = cv2.imread("stop.png", 0)

    # Perform template matching
    res_forward = cv2.matchTemplate(gray, forward_template, cv2.TM_CCOEFF_NORMED)
    res_backward = cv2.matchTemplate(gray, backward_template, cv2.TM_CCOEFF_NORMED)
    res_right = cv2.matchTemplate(gray, right_template, cv2.TM_CCOEFF_NORMED)
    res_left = cv2.matchTemplate(gray, left_template, cv2.TM_CCOEFF_NORMED)
    res_stop = cv2.matchTemplate(gray, stop_template, cv2.TM_CCOEFF_NORMED)

    # Define threshold for template matching
    threshold = 0.8

    # Check if any sign is detected
    if np.max(res_forward) > threshold:
        return 'forward'
    elif np.max(res_backward) > threshold:
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

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
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
                send_command('d\n')  # Right
                print("right detected")
            elif sign == 'left':
                send_command('a\n')  # Left
                print("left detected")
            elif sign == 'stop':
                send_command('x\n')  # Stop
                print("stop detected")

        # Display the frame
        cv2.imshow('Frame', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release webcam and close all windows
cap.release()
cv2.destroyAllWindows()
