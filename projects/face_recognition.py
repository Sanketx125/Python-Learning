import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml')


# Start capturing video from the camera
cap = cv2.VideoCapture(0)

# Initialize an empty dictionary to store the face data
face_data = {}

# Loop over the frames captured from the camera
while True:
    # Read the next frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Loop over each face detected
    for (x, y, w, h) in faces:
        # Extract the face region from the frame
        face_roi = frame[y:y+h, x:x+w]

        # Ask the developer to enter the name of this person
        name = input('Please enter the name of this person: ')

        # Save the face data with the person's name as the key
        face_data[name] = face_roi

        # Display the face region with a rectangle and label showing the person's name
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the video feed with the detected faces and names
    cv2.imshow('Video Feed', frame)

    # Wait for the user to press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()

# Save the face data to a file for future use
with open('face_data.pkl', 'wb') as f:
    pickle.dump(face_data, f)
