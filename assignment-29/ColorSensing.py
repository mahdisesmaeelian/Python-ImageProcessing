import numpy as np
import cv2

video_cap = cv2.VideoCapture(0)

while True:
    ret,frame = video_cap.read()

    myrec = frame[180:300,270:390]

    if ret == False:
        break
 
    kernel = np.ones((35,35),np.float32)/1225
    dst = cv2.filter2D(frame,-1,kernel)

    cv2.rectangle(frame,(270,180), (390,300), (0, 0, 0),2)
    dst[180:300,270:390] = myrec

    if  0 < np.average(myrec) <= 60:
        cv2.putText(dst, "Black", (25, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3) 
    elif 60 < np.average(myrec) <= 120:
        cv2.putText(dst, "Gray", (25, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3)
    else:
        cv2.putText(dst, "White", (25, 50), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0),3) 

    cv2.imshow('Camera',dst)
    cv2.waitKey(1)                 