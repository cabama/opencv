import numpy as np
import cv2
RUTA_VIDEO = "rosources/video"

cap = cv2.VideoCapture('asimo.avi')

while(True):
    exito, frame = cap.read()
    print exito
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()