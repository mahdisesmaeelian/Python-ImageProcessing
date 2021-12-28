import numpy as np
import cv2

list_frames = []
y = 1

cam = cv2.VideoCapture(0)

while True:

    ret,frame = cam.read()

    if not ret:
        break
    
    rows , cols , _= frame.shape

    list_frames.append(frame[y-1])
    frame[:y, :] = np.array(list_frames)

    cv2.line(frame, (0, y), (cols, y), (238,0,0), 1)
    y += 1

    if cv2.waitKey(1) == ord('q'):
        break

    if y == rows :
        break

    cv2.imshow("Camera", frame)
    cv2.waitKey(1)

cv2.imwrite("Time warp scan.jpg",frame)