import numpy as np
import cv2

img = cv2.imread('input/flower_input.jpg', 0)

threshold = 180
result = np.zeros(img.shape)
mask = np.ones((15,15)) / 225
rows , cols = img.shape

for i in range (7,rows-7):
    for j in range(7,cols-7):          
        small_img = img[i-7:i+8,j-7:j+8]
        result[i,j] = np.sum(small_img * mask)

for i in range(rows):
    for j in range(cols):
        if img[i,j] <= threshold: 
            img[i,j] = result[i,j]
                   
cv2.imwrite("Portrate_Flower.png", img)
cv2.waitKey()