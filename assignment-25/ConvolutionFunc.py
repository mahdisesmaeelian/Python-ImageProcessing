import numpy as np
import cv2

img = cv2.imread("input/me.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

result = np.zeros(img.shape)

def Canvolution(a):
    b = a//2
    mask = np.ones((a,a)) / (a*a)

    rows , cols = img.shape

    for i in range (b,rows-b):
        for j in range(b,cols-b):
            small_img = img[i-b:i+(b+1), j-b:j+(b+1)]
            result[i,j] =np.sum(small_img * mask)

Canvolution(15)

cv2.imwrite("result_me.jpg",result)
