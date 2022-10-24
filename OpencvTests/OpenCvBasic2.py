from configparser import Interpolation
from tkinter import Frame
from turtle import width
import cv2 as cv
img = cv.imread('Resources/Photos/cat.jpg')
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

#maken een functie aan die vraagt voor frame en 'scale' voor de grote van je img,video of live video te veranderen
def rescaleFrame(frame, scale=0.75):
    #shape index 1 is de breedte van je window(maal de schaal)(int)
    width = int(frame.shape[1]*scale)
    #shape index 0 is de hoogte van je window(maal de schaal)(int)
    height = int(frame.shape[0]*scale)
    #dimensie variabel met je hoogte en breedte
    dimensions = (width,height)
    #geeft de frame geresized weer
    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)

#resulotie veranderen alleen voor live video
def resChange(width,height):
    capture.set(3,width)
    capture.set(4,height)


#code van voorgaande oefening + een extra window voor de gerescalde frames
resized_image = rescaleFrame(img)
cv.imshow('Cat', img)
cv.imshow('Resized_cat',resized_image)


while True:
    isTrue, frame = capture.read()    

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video_Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
cv.destroyAllWindows()