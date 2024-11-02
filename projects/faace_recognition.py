import cv2
video_cap = cv2.VideoCapture(0)
while True: 
    ret , video_data = video_cap.read()
    cv2.imshow("face recognition", video_data)

    if cv2.waitKey(10) = ord():
        break

    video_cap.release() 