import cv2
import sys

img_abierta = cv2.imread('prueba.jpg',0)
cv2.imshow("Curso de OpenCV", img_abierta)

def cerrarVentana():
	cv2.destroyAllWindows()
	sys.exit()

def guardar_imagen():
	cv2.imwrite("demo_saved.jpg", img_abierta)

tecla_pulsada = cv2.waitKey(0)

if tecla_pulsada == ord('s'):
	guardar_imagen()
	cerrarVentana()
else:
	cerrarVentana()
