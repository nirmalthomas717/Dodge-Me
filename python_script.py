#Face tracker using OpenCV and Arduino
import cv2
import sys
import logging as log
import datetime as dt
import urllib.request
import numpy as np
import serial,time
from time import sleep

#fourcc= cv2.VideoWriter_fourcc(*'XVID')
ArduinoSerial=serial.Serial('COM6',9600,timeout=0.1)
#out= cv2.VideoWriter('face detection4.avi',fourcc,20.0,(640,480))
time.sleep(1)

frame = None
key = None
anterior = 0

print ('START')

while True:
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    log.basicConfig(filename='webcam.log',level=log.INFO)
    imgResponse = urllib.request.urlopen ('http://192.168.4.1/capture?')
    imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    frame =cv2.imdecode (imgNp, -1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
    )

    for x,y,w,h in faces:
        #sending coordinates to Arduino
        string='X{0:d}Y{1:d}'.format((x+w//2),(y+h//2))
        print(string)
        ArduinoSerial.write(string.encode('utf-8'))
        #plot the center of the face
        cv2.circle(frame,(x+w//2,y+h//2),2,(0,255,0),2)
        #plot the roi
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    #plot the squared region in the center of the screen
    cv2.rectangle(frame,(640//2-30,480//2-30),
                 (640//2+30,480//2+30),
                  (255,255,255),3)
    #out.write(frame)
    cv2.imshow('img',frame)
    #cv2.imwrite('output_img.jpg',frame)
    '''for testing purpose
    read= str(ArduinoSerial.readline(ArduinoSerial.inWaiting()))
    time.sleep(0.05)
    print('data from arduino:'+read)
    '''
    # press q to Quit
    if cv2.waitKey(10)&0xFF== ord('q'):
        break
cv2.destroyAllWindows()
