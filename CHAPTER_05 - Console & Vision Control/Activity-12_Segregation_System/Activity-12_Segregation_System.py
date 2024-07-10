#pip install opencv-python-headless
#pip install opencv-python
#pip install pyserial

import cv2
import serial

def main():
    # Initialize serial connection with arduino_ide
    try:
        arduino_ide = serial.Serial('COM6', 9600) #Change it
    except serial.SerialException as e:
        print("Error:", e)
        return
    
    def control_servo(image_choice):
        command = b'1' if image_choice == 1 else b'0'
        arduino_ide.write(command)
        print("Sent '{}' to arduino_ide to move servo {}".format(command, "clockwise" if image_choice == 1 else "anticlockwise"))

    def capture_and_detect_images():
        cap = cv2.VideoCapture(0)  # Initialize camera
        # Load predefined images (optional)
        forward_img = cv2.imread('forward.jpg', 0)  # Load as grayscale
        backward_img = cv2.imread('backward.jpg', 0)  # Load as grayscale

        # Check if images are loaded properly
        if forward_img is None or backward_img is None:
            print("Error: Could not load one or both template images.")
            return None

        image_choice = None
        while True:
            ret, frame = cap.read()  # Capture frame from camera

            if not ret:
                print("Failed to capture image")
                break

            # Convert frame to grayscale for template matching
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Check the size of the template images and resize if necessary
            if forward_img.shape[0] > gray_frame.shape[0] or forward_img.shape[1] > gray_frame.shape[1]:
                scale_factor = min(gray_frame.shape[0] / forward_img.shape[0], gray_frame.shape[1] / forward_img.shape[1])
                forward_img = cv2.resize(forward_img, (int(forward_img.shape[1] * scale_factor), int(forward_img.shape[0] * scale_factor)))
            
            if backward_img.shape[0] > gray_frame.shape[0] or backward_img.shape[1] > gray_frame.shape[1]:
                scale_factor = min(gray_frame.shape[0] / backward_img.shape[0], gray_frame.shape[1] / backward_img.shape[1])
                backward_img = cv2.resize(backward_img, (int(backward_img.shape[1] * scale_factor), int(backward_img.shape[0] * scale_factor)))

            # Perform template matching
            forward_match = cv2.matchTemplate(gray_frame, forward_img, cv2.TM_CCOEFF_NORMED)
            backward_match = cv2.matchTemplate(gray_frame, backward_img, cv2.TM_CCOEFF_NORMED)

            # Define threshold for matching score
            threshold = 0.8
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
        arduino_ide.close()  # Close serial connection

if __name__ == "__main__":
    main()
