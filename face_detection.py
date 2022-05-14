import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
  ref, frame = cap.read()

  grayColorFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(grayColorFrame, 1.3, 5)

  for face in faces:
    x, y, w, h = face.ravel()
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 10)

  cv2.imshow('frame', frame)
    
  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()