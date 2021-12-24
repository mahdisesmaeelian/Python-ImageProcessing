import argparse
import cv2
import matplotlib.pyplot as plt
import imutils
from imutils import contours
from imutils.perspective import four_point_transform

parser = argparse.ArgumentParser(description="Sudoku Detector version 1.0")
parser.add_argument("--input" , type=str , help="path of your input image")
parser.add_argument("--filter_size" , type=int , help="size of GaussianBlur mask", default= 7)
parser.add_argument("--output" , type=str , help="path of your output image")
args = parser.parse_args()

img = cv2.imread(args.input)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred_img = cv2.GaussianBlur(gray_img , (args.filter_size,args.filter_size), 3)

thresh = cv2.adaptiveThreshold(blurred_img , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV , 11 ,2)

contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

contours = imutils.grab_contours(contours)
contours = sorted(contours , key = cv2.contourArea , reverse = True)

sudoku_contour = None

for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour , True)
    approx = cv2.approxPolyDP(contour , epsilon , True)
                              
    if len(approx) == 4:
        sudoku_contour = approx
        break

if sudoku_contour is None :
    print("Not found")
else:
    result = cv2.drawContours(img , [sudoku_contour] , -1 ,(0,255,0) , 8)
    puzzle = four_point_transform(img, sudoku_contour.reshape(4,2))
    warped = four_point_transform(gray_img, sudoku_contour.reshape(4,2))
    cv2.imshow("Puzzle" ,puzzle)
    cv2.imwrite(args.output, puzzle)