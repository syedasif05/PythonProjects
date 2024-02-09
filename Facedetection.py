# import cv2
#
# video_capture = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = video_capture.read()
#
#     if not ret:
#         print("Failed to capture frame. Exiting...")
#         break
#
#     # Display the frame
#     cv2.imshow('Video', frame)
#
#     if cv2.waitKey(10) == ord("a"):
#         break
#
# video_capture.release()
# cv2.destroyAllWindows()

import cv2

# Load the pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    # Capture video frame
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame with face detection
    cv2.imshow('Video with Face Detection', frame)

    # Break the loop if 'a' is pressed
    if cv2.waitKey(10) == ord("a"):
        break

# Release the video capture object
video_capture.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
