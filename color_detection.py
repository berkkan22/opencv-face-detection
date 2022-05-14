import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
  ref, frame = cap.read()

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  # HSC color map https://i.stack.imgur.com/TSKh8.png
  lower_blue = np.array([90, 50, 50])
  upper_blue = np.array([130, 255, 255])

  lower_red = np.array([170, 200, 50])
  upper_red = np.array([180, 255, 255]) 

  mask = cv2.inRange(hsv, lower_red, upper_red)

  result = cv2.bitwise_and(frame, frame, mask=mask)

  cv2.imshow('frame', result)
  cv2.imshow('mask', mask)

  if cv2.waitKey(1) == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

# BGR_color = np.array([[[0, 0, 255]]])
# cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)