import cv2 as cv
import numpy as np

#een image word gegenereerd dat 500x500 3 kleur kanalen(rgb) is(blanko)
blank = np.zeros((500,500,3), dtype='uint8')
#zet alle pixels een bepaalde rgb value
 #blank[:] = 0,125,75

#zet bepaalde pixels in een rgb value YxZ
#blank[0:500,166:333]= 0,255,255
#blank[0:500,333:500]= 0,0,255

#een driehoek(frame,punt1(x,y),punt2(x,y),kleur,dikte)
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)
#een circle tekenen(frame,origin middlepunt,straal,kleur,dikte)
cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
#een lijn tekenen(frame,punt1(x,y),punt2(x,y),kleur,dikte)
cv.line(blank,(0,250),(500,250),(255,0,0),thickness=2)
#een tekst tekenen(frame,txt,positie,Font,groote,dikte)
cv.putText(blank,"Hello World",(0,250),cv.FONT_HERSHEY_SCRIPT_COMPLEX,3.0,(0,255,255),thickness=2)
cv.imshow("Blank",blank)



cv.waitKey(0)
