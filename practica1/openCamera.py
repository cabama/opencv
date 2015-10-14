# Importamos las librerias necesarias
import numpy as np
import cv2

# Abrimos la webcam y asignamos este objeto a una variable.
cap = cv2.VideoCapture(0)

# Entramos en un  bucle
while(True):

    # capturamos el frame actual
    ret, frame = cap.read()

    # Convertimos este frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mostramos el frame en escala de grises
    cv2.imshow('frame',gray)

    # Si se pulsa la tecla 'Q' se saldra del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tras haber salido del bucle, liberamos la camara y cerramos todas las ventanas.
cap.release()
cv2.destroyAllWindows()