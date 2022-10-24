#openCv import met Genoemt tot cv
import cv2 as cv
#leest de pixels binnen van Cat photo (in variabel img)
img = cv.imread('Resources/Photos/cat.jpg') 
#maakt een window aan naam 'Picture en displayed img
cv.imshow('Picture',img)
#wacht voor een bepaalde tijd tot er een key input is gebeurd 0 = inf.(dan sluit hij het venster)
cv.waitKey(0)