import cv2

# Leemos la imagen y la introducimos en la siguiente variable.
img_abierta = cv2.imread('resources/images/prueba.jpg', 0)
# Abrimos una ventana de tipo imagen, se introduce el titulo y la variable que contiene la imagen.
cv2.imshow("Curso de OpenCV", img_abierta)


# Definimos una funcion para cerrar  la ventana abierta
def cerrar_ventana():
    cv2.destroyAllWindows()


# Definimos una funcion para guardar la imagen, se le pasa como parametros el nombre para guardar y la variable imagen.
def guardar_imagen():
    cv2.imwrite("saved/demo_saved.jpg", img_abierta)


# Escuchamos que se pulse una tecla
tecla_pulsada = cv2.waitKey(0)
# Si la tecla pulsada es S se guarda la imagen y se cierra
if tecla_pulsada == ord('s'):
    guardar_imagen()
    cerrar_ventana()
# Si se pulsa cualquier otra tecla se cierra la imagen.
else:
    cerrar_ventana()
