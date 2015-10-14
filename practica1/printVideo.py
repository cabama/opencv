import numpy as np
import cv2

def dibujar_rectangulo(img):
	img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
	return img

def escribir(escrito, img):	
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,escrito,(10,500), font, 4,(255,255,255),2,cv2.CV_AA)

#img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
#img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    escribir("PALETO DEL DIA", gray)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


