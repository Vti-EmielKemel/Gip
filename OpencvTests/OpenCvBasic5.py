import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)

while True:
    isTrue, frame = cap.read()
    
    #Breedte word gecast naar int(float is nutteloos)
    width = int(cap.get(3))
    #Hoogte word gecast naar int(float is nutteloos)
    height = int(cap.get(4))
    #frame omzetten in hsv
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    #hsv val dat het tussen zal moeten zitten
    Upper_green = np.array([83,255,255])
    Lower_Green = np.array([25,40,40])
    #mask alles tussen de waarden
    mask = cv.inRange(hsv,Lower_Green,Upper_green) 
    #mask over je origineel beeld 
    einde = cv.bitwise_and(frame,frame,mask=mask)   
    cv.imshow("mask",mask)
    cv.imshow('ded', hsv)
    cv.imshow('Video', einde)
    if cv.waitKey(1) & 0xFF==ord('d'):
        break
cap.release()
cv.destroyAllWindows()