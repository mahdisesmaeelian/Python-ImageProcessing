import numpy as np
import cv2

blurred = False
rotated = False
EmojiOnFace = False
SunglassesMustache = False

face_detector = cv2.CascadeClassifier("src/haarcascade_frontalface_default.xml")
eyes_detector = cv2.CascadeClassifier('src/frontalEyes35x16.xml')
nose_detector  = cv2.CascadeClassifier('src/Nose18x15.xml')

sticker1 = cv2.imread("img/emoji1.png")
mustache = cv2.imread('img/mustache.png')
sunglasses = cv2.imread('img/sunglasses.png')

video_cap = cv2.VideoCapture(0)

while True:
    
    ret,frame = video_cap.read()
    if ret == False:
        break

    faces = face_detector.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)
    
    for (x, y, w, h) in faces:

        face_pos = frame[y:y+h, x:x+w]
        eyes = eyes_detector.detectMultiScale(face_pos, scaleFactor=1.2, minNeighbors=5)
        nose = nose_detector.detectMultiScale(face_pos, scaleFactor=1.5, minNeighbors=5)
        roi = frame[y:y+h, x:x+h]

        if EmojiOnFace:
            sticker = cv2.resize(sticker1, (w,h))
            _,mask= cv2.threshold(sticker,25,255,cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)

            background1 = cv2.bitwise_and(roi,roi,mask = mask_inv)
            mask_sticker = cv2.bitwise_and(sticker, sticker, mask=mask)

            finalsticker =cv2.add(mask_sticker ,background1)
            frame[y:y+h, x:x+h] = finalsticker

        if SunglassesMustache:
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(face_pos, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3) 
                sunglasses1 = cv2.resize(sunglasses, (ew,eh))
                face_pos[ey:ey+eh, ex:ex+ew] = sunglasses1
                
            for (nx, ny, nw, nh) in nose:
                cv2.rectangle(face_pos, (nx, ny), (nx + nw, ny + nh), (255, 0, 0), 3)
                mustache1 = cv2.resize(mustache, (nw,nh))
                face_pos[ny:ny+nh, nx:nx+nw] = mustache1
        
        if blurred:
            frame[y:y+h, x:x+h] = cv2.blur(frame[y:y+h, x:x+h], (25, 25))
            
        if rotated:
            frame[y:y+h, x:x+h] = cv2.rotate(frame[y:y+h, x:x+h], cv2.ROTATE_180)

        
    key = cv2.waitKey(1)

    if key == ord('1'):
        EmojiOnFace = not EmojiOnFace

    if key == ord('2'):
        SunglassesMustache  = not SunglassesMustache 

    if key == ord('3'):
        blurred = not blurred

    if key == ord('4'):
        rotated = not rotated

    cv2.imshow('Camera',(frame))
    cv2.waitKey(1)
