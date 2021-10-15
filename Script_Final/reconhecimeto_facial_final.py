import cv2
import numpy as np
from time import sleep

COLOR = (255, 0, 0)
STROKE = 2
COUNT = 0

xml_path = 'haarcascade_frontalface_alt2.xml'

clf = cv2.CascadeClassifier(cv2.data.haarcascades + xml_path)
cap = cv2.VideoCapture(0)

while (not cv2.waitKey(20) & 0xFF == ord('q')):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = clf.detectMultiScale(gray)
    print(faces)
    # Quando encontrar um rosto
    # if faces != ():
    #     x,y,w,h = faces[0]
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), COLOR, STROKE)
    #     cv2.imwrite('opencv_'+str(faces)+'.png',frame)
    #     print(f"Detectei!! ${faces}")
    #     sleep(3)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), COLOR, STROKE)
    cv2.imshow('Video', frame)
cap.release()
cv2.destroyAllWindows()