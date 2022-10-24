#openCv import met Genoemt tot cv
import cv2 as cv

#foto binnen lezen

#leest de pixels binnen van Cat photo (in variabel img)
# img = cv.imread('Resources/Photos/cat.jpg') 
#maakt een window aan naam 'Picture en displayed img
# cv.imshow('Picture',img)
#wacht voor een bepaalde tijd tot er een key input is gebeurd 0 = inf.(dan sluit hij het venster)
# cv.waitKey(0)

#video binnenlezen

#leest de pixels binnend van de video (var capture)
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    #leest de frames binnen van de video en een bool dat zegt of de frame succesvol binnengelezen is
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    #Als 20 seconden voorbij zijn of d word in gedrukt break de loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
#geeft error als te lang wacht door geen frames meer