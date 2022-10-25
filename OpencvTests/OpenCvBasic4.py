import cv2 as cv
from cv2 import INTER_LINEAR
img = cv.imread('Resources/Photos/cat.jpg')

#maakt img grijs
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#blurred de img
blur = cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
#vertoont de uitlijn
canny = cv.Canny(img,125,175)
#uitzetten van img
dil = cv.dilate(img,(9,9),iterations=10)
#Erosief effect
erode = cv.erode(canny,(9,9),iterations=1)
#Grote veranderen (inter linear/Cubic(vergroot),inter area(verklein))
andere = cv.resize(img,(1080,720),interpolation=INTER_LINEAR)


cv.imshow("erode",erode)
cv.imshow("Dil",dil)
cv.imshow("Canny",canny)
cv.imshow("BLUR",blur)
cv.imshow("gray",gray)
cv.imshow("Normaal",img)
cv.imshow("andere",andere)
cv.waitKey(0)