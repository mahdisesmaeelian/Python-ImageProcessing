import argparse
import cv2
import matplotlib.pyplot as plt
import imutils
from imutils import contours
from imutils.perspective import four_point_transform

cam = cv2.VideoCapture(0)

while True:

    ret,frame = cam.read()

    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blurred_img = cv2.GaussianBlur(gray_frame , (3,3), 3)

    thresh = cv2.adaptiveThreshold(blurred_img , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV , 11 ,2)

    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

    contours = imutils.grab_contours(contours)
    contours = sorted(contours , key = cv2.contourArea , reverse = True)

    sudoku_contour = None

    for contour in contours:
        epsilon = 0.12 * cv2.arcLength(contour , True)
        approx = cv2.approxPolyDP(contour , epsilon , True)
                                
        if len(approx) == 4:
            sudoku_contour = approx
            break

    if sudoku_contour is None :
        print("Not found")
    else:
        result = cv2.drawContours(frame , [sudoku_contour] , -1 ,(0,255,0) , 8)

    cv2.imshow("Camera", frame)


    if cv2.waitKey(1) == ord('s'):
        if sudoku_contour is None :
            print("Not found")
        else:
            puzzle = four_point_transform(frame, sudoku_contour.reshape(4,2))
            warped = four_point_transform(gray_frame, sudoku_contour.reshape(4,2))
            cv2.imwrite("Detected_Sudoku.jpg" , puzzle)

    if cv2.waitKey(1) == ord('q'):
        break