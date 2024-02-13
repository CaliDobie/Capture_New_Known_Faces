import os
import cv2
import keyboard

def take_and_save_picture(folder_path):
    # Open a connection to the camera (0 is the default camera)
    camera_capture = cv2.VideoCapture(0)
    camera_capture.set(cv2.CAP_PROP_FPS, 60)  # sets the frame rate

    while True:
        # Capture a single frame
        ret, frame = camera_capture.read()

        # Display the frame in a preview window
        cv2.imshow("Camera Preview - Press 'Tab' to capture a new Known Face", frame)

        # Check for tab key press
        if keyboard.is_pressed("tab"):
            # Allow the user to input a name for the image
            image_name = input("Enter a name for the new Known Face: ") + ".jpg"

            # Specify the path where the image will be saved
            image_path = os.path.join(folder_path, image_name)

            # Save the captured frame as an image
            cv2.imwrite(image_path, frame)

            print(f"New Known Face '{image_name.split(".")[0]}' saved in '{folder_path}'. \n")

        # Check for 'Esc' key press to exit
        elif cv2.waitKey(1) & 0xFF == 27:
            break

    # Release the camera and close OpenCV windows
    camera_capture.release()
    cv2.destroyAllWindows()

# Example usage:
folder_path = "\your\folder\path\here"
take_and_save_picture(folder_path)
