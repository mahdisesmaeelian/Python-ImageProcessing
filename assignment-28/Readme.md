## Sudoku detector using opencv 

The following code is a Python program that can be run at the command line ,It takes input image and output name from user :

◾Convert bgr color to gray

◾Using GaussianBlur for decrease noises

![2021-12-24_22-00-15](https://user-images.githubusercontent.com/88204357/147368827-de6a6c28-5429-4e20-9bf3-5061eda2ee19.png)

◾Adaptive threshold to obtain binary image

![2021-12-24_22-00-23](https://user-images.githubusercontent.com/88204357/147368846-e1a0658a-25eb-411c-ae25-67d94bfff2ac.png)


◾Find contours and filter for largest contour

◾Find shape with 4 points by approxPolyDP

◾Draw contours around the sudoku table 

![2021-12-24_22-00-33](https://user-images.githubusercontent.com/88204357/147368851-fa47ab42-2270-40bb-8650-5033dfe32efd.png)


◾Crop the table and save it as a jpg image


![2021-12-24_22-00-43](https://user-images.githubusercontent.com/88204357/147368852-b92db110-d2d2-4242-9bfe-1dd94f3c3c2d.png)

## Webcam Sudoku Detector.py


This python project has an ability to recognize Sudoku table in live webcam.

By pressing the s button, the sudoku image is cropped and saved.

![2021-12-24_20-31-28](https://user-images.githubusercontent.com/88204357/147369098-47c77bad-e3ac-4e96-9fab-ecfd8183a20c.png)

![2021-12-24_20-30-17](https://user-images.githubusercontent.com/88204357/147369100-555d65de-57de-4a30-a80f-ff386a632a02.png)
