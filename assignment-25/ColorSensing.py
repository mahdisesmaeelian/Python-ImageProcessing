import numpy as np
import cv2

video_cap = cv2.VideoCapture(0)

while True:
    ret,frame = video_cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    myrec = frame[180:300,270:390]
      
    if ret == False:
        break
 
    kernel = np.ones((35,35),np.float32)/1225
    dst = cv2.filter2D(frame,-1,kernel)

    cv2.rectangle(frame,(270,180), (390,300), (0, 0, 0),2)
    dst[180:300,270:390] = myrec
    color_detect_area = dst[180:300,270:390]

    rows , cols = color_detect_area.shape

    for i in range(rows):
        for j in range(cols):
            if dst[i,j] >= 200:
                print('yes') 

    cv2.imshow('Camera',dst)
    cv2.waitKey(1)                 