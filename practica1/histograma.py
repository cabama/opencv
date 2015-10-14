'''
PRACTICA: Histograma de una imagen en color.
Autor: Carlos Barreiro Mata
'''

# Importamos las librerias necesarias
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Variable que contiene la ruta de la imagen
IMAGEN = "resources/images/prueba.jpg"

# Leemos la imagen y la guardamos en la variable img
img = cv2.imread(IMAGEN)

# Creamos una tupla (array) que contiene los caracteres: b,g,r
color = ('b','g','r')

# bucle que recorre el vector color.
# En su recorrido define a su elemento como col.
# i en su recorrido es el indice, por ejemplo, b es 0, g es 1, r es 2.
for i,col in enumerate(color):
	# Obtenemos el histograma de la imagen (BGR) la capa i de 0 a 256 valores
	histr = cv2.calcHist([img],[i],None,[256],[0,256])
	# Predibujamos en la libreria plt el histograma actual
	plt.plot(histr,color = col)
	# Indicamos el rango del eje X a mostrar
	plt.xlim([0,256])

# Finalmente dibujamos la grafica
plt.show()