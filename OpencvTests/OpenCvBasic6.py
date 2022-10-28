from cv2 import COLOR_BGR2GRAY
import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

while True:
    isTrue, frame = cap.read()
    grijs = cv.cvtColor(frame,COLOR_BGR2GRAY)
    hoeken = cv.goodFeaturesToTrack(grijs,50,0.3,10)
    #zet alle hoek coordinaten in een int
    hoeken = np.int0(hoeken)
    for hoek in hoeken: 
        #verwijderd alle overbodige [] en steekt de coordinaten in een variabel
        x, y = hoek.ravel()
        #tekent circles op de hoeken
        cv.circle(frame,(x,y),5,(0,0,255),-1)
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF==ord('d'):
        break
    
cap.release()
cv.destroyAllWindows()