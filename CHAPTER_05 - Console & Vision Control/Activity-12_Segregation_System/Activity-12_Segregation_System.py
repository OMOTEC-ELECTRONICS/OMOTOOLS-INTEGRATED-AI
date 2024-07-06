#pip install opencv-python
#Pip install pyserial

import cv2
import serial

def main():
    # Initialize serial connection with Arduino Ide
    try:
        arduino = serial.Serial('COM69', 9600)
    except serial.SerialException as e:
        print("Error:", e)
        return

    def control_servo(image_choice):
        command = b'1' if image_choice == 1 else b'0'
        arduino.write(command)
        print("Sent '{}' to Arduino to move servo {}".format(command, "clockwise" if image_choice == 1 else "anticlockwise"))

    def capture_and_detect_images():
        cap = cv2.VideoCapture(0)  # Initialize camera

        # Load predefined images (optional)
        forward_img = cv2.imread('forward2.jpg', 0)  # Load as grayscale
        backward_img = cv2.imread('backward2.jpg', 0)  # Load as grayscale

        image_choice = None

        while True:
            ret, frame = cap.read()  # Capture frame from camera

            # Convert frame to grayscale for template matching
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Perform template matching
            forward_match = cv2.matchTemplate(gray_frame, forward_img, cv2.TM_CCOEFF_NORMED)
            backward_match = cv2.matchTemplate(gray_frame, backward_img, cv2.TM_CCOEFF_NORMED)

            # Define threshold for matching score
            threshold = 0.8

            # Check if template matches are found
            if cv2.minMaxLoc(forward_match)[1] > threshold:
                image_choice = 1
                print("Forward image detected")
                break
            elif cv2.minMaxLoc(backward_match)[1] > threshold:
                image_choice = 2
                print("Backward image detected")
                break

            # Display camera feed
            cv2.imshow('Camera Feed', frame)

            key = cv2.waitKey(1) & 0xFF  # Get user input (keyboard)
            if key == ord('q'):  # Close windows on 'q' press
                break

        cap.release()  # Release camera resources
        cv2.destroyAllWindows()

        return image_choice

    try:
        while True:
            image_choice = capture_and_detect_images()
            if image_choice is not None:
                control_servo(image_choice)
                break
    except KeyboardInterrupt:
        pass
    finally:
        arduino.close()  # Close serial connection

if __name__ == "__main__":
    main()
