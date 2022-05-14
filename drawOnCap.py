import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
  ref, frame = cap.read()
  width = frame.shape[1]
  height = frame.shape[0]

  line = cv2.line(frame, (0, 0), (width, height), (0, 255, 0), 5)
  line2 = cv2.line(frame, (0, height), (width, 0), (0, 255, 0), 10)
  rect = cv2.rectangle(frame, (100, 100), (200, 200), (128, 128, 128), 5)
  # -1 füllt den kreis oder auch das rechteck werte über 0 sind die dicke der linie
  kreis = cv2.circle(frame, (width//2, height//2), 60, (0, 255, 255), -1)
  font = cv2.FONT_HERSHEY_SIMPLEX
  text = cv2.putText(frame, "Hallo Welt!", (280, 250), font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)

  cv2.imshow('frame', frame)
    
  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()