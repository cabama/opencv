import numpy as np
import cv2

"""Espacio para las funciones"""
# Dibujamos un rectangulo en el frame
def dibujar_rectangulo(img):
	img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
	return img
# Escribimos el texto pasado en el frame
def escribir(escrito, img):
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,escrito,(10,500), font, 4,(255,255,255),2,cv2.CV_AA)

#img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
#img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)


"""Comenzamos el Script"""

# Cargamos el video en una variable
VIDEO_RUTA = "resources/video/asimo.avi"
MENSAJE="Texto a escribir"
cap = cv2.VideoCapture(VIDEO_RUTA)

# Mostramos mensaje informativo
if cap.isOpened() == True:
	print("Video correctamente cargado")
else:
	print("Error en la carga del video")


# Comenzamos el bucle de produccion
while(cap.isOpened()):
    # Capturamos el frame actual
    ret, frame = cap.read()
    # Convertimos a blanco y negro
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Imprimimos el mensaje en este frame
    escribir(MENSAJE, gray)
    # Mostramos la imagen capturada modificada
    cv2.imshow('frame',gray)
	# Si pulsamos el caracter q salimos del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Tras haber salido del bucle libreamos la webcam y cerramos las ventanas
cap.release()
cv2.destroyAllWindows()
