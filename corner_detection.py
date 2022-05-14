from turtle import circle
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
  ref, frame = cap.read()

  grayColorFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  corners = cv2.goodFeaturesToTrack(grayColorFrame, 1000, 0.01, 20)
  corners = np.int0(corners)

  for corner in corners:
    x, y = corner[0][0], corner[0][1] 
    cv2.circle(frame, (x, y), 5, (0, 255, 255), -1)

  cv2.imshow('frame', frame)

  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()