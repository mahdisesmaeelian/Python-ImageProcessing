import numpy as np
import cv2

min_HSV = np.array([0, 48, 80], dtype = "uint8")
max_HSV = np.array([20, 255, 255], dtype = "uint8")

video_cap = cv2.VideoCapture(0)

while True:

	ret,frame = video_cap.read()
    
	frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	Mask = cv2.inRange(frame_HSV, min_HSV, max_HSV)

	skinMask = cv2.GaussianBlur(Mask, (3, 3), 0)
	output = cv2.bitwise_and(frame, frame, mask = skinMask)

	cv2.imshow("Camera", output)

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break