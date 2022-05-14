import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(frame.shape[1])
    height = int(frame.shape[0])
    
    # image = np.zeros([frame.shape[0]*2,frame.shape[1]*2], np.uint8)
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, :width//2] = cv2.flip(smaller_frame, 1)
    image[height//2:, width//2:] = smaller_frame
    
    cv2.imshow('frame', image)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
