import numpy as np
import cv2 as cv

img = cv.imRead("Resources/Photos/soccer_practice.jpg",0)
ball = cv.imRead("Resources/Photos/ball.png",0)   
img2 = img.copy()

cv.imshow("Img",img)