import cv2

blurred = False
rotated = False
EmojiOnFace = False
SunglassesMustache = False

face_detector = cv2.CascadeClassifier("src/haarcascade_frontalface_default.xml")
eyes_detector = cv2.CascadeClassifier('src/frontalEyes35x16.xml')
mouth_detector  = cv2.CascadeClassifier('src/mouth.xml')

sticker1 = cv2.imread("img/emoji1.png")
lip = cv2.imread('img/lips.png')
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
        mouth = mouth_detector.detectMultiScale(face_pos, scaleFactor=1.3, minNeighbors=50)

        if EmojiOnFace:
            
            sticker = cv2.resize(sticker1, (w,h))
            img2gray = cv2.cvtColor(sticker,cv2.COLOR_BGR2GRAY)

            _,mask= cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)

            background1 = cv2.bitwise_and(face_pos,face_pos,mask = mask_inv)
            mask_sticker = cv2.bitwise_and(sticker, sticker, mask=mask)

            finalsticker =cv2.add(mask_sticker ,background1)
            frame[y:y+h, x:x+h] = finalsticker

        if SunglassesMustache:
            for (ex, ey, ew, eh) in eyes:

                sunglasses_resize = cv2.resize(sunglasses, (ew,eh))
                sunglasses2gray = cv2.cvtColor(sunglasses_resize,cv2.COLOR_BGR2GRAY)

                _,mask= cv2.threshold(sunglasses2gray,10,255,cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)

                eyes_pos = cv2.bitwise_and(face_pos[ey:ey+eh, ex:ex+ew],face_pos[ey:ey+eh, ex:ex+ew],mask = mask)
                mask_glasses = cv2.bitwise_and(sunglasses_resize, sunglasses_resize, mask=mask_inv)

                finalsticker =cv2.add(mask_glasses ,eyes_pos)
                face_pos[ey:ey+eh, ex:ex+ew] = finalsticker
                
            for (mx, my, mw, mh) in mouth:

                mouth_resize = cv2.resize(lip, (mw,mh))
                mouth2gray = cv2.cvtColor(mouth_resize,cv2.COLOR_BGR2GRAY)

                _,mask = cv2.threshold(mouth2gray,10,255,cv2.THRESH_BINARY)
                mask_inv = cv2.bitwise_not(mask)

                nose_pos = cv2.bitwise_and(face_pos[my:my+mh, mx:mx+mw],face_pos[my:my+mh, mx:mx+mw],mask = mask_inv)
                mask_mouth = cv2.bitwise_and(mouth_resize, mouth_resize, mask=mask)

                finalmouth =cv2.add(mask_mouth ,nose_pos)
                face_pos[my:my+mh, mx:mx+mw] = finalmouth
        
        if blurred:
            for (x, y, w, h) in faces:
                square = cv2.resize(frame[y:y+h,x:x+w], (10,10))
            output = cv2.resize(square, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+h] = output
                                  
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