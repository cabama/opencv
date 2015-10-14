import cv2
import sys

# Tomamos el modelo de cara de referencia
cascPath = 'model_face.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

# Predisponemos a capturar el video
cap = cv2.VideoCapture(0)

# Funcion para escribir en una imagen si se encuentra paleto
def escribir(escrito, img):	
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img,escrito,(20,80), font, 4,(255,255,255),2,cv2.CV_AA)

# Funcion para detectar caras en la imagen.
def detector_faces(frame, faceCascade):
	faces = faceCascade.detectMultiScale(
	    frame,
	    scaleFactor=1.1,
	    minNeighbors=5,
	    minSize=(30, 30),
	    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
	)
	return faces


cont = 0

# Bucle para procesar frame a frame
while(True):

	# Obtenemos el frame de la webcam
	ret, frame = cap.read()

	# Lanzamos algoritmo para detectar face cada 3 frames
	if cont == 0:
		faces = detector_faces(frame, faceCascade)

		# Escribimos cuantas caras se han detectado
		numeroCaras = len(faces)

		if numeroCaras == 1:
			escribir("Paleto detectado", frame)
		elif numeroCaras > 1:
			escribir("Demasiados Paletos", frame)

		# Dibujamos un triangulo para las caras
		for (x, y, w, h) in faces:
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

		# Representamos todo en la Ventana, salimos si se pulsa Q.
		cv2.imshow("Detectos de paletos", frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cont += 1

	if cont == 5:
		cont = 0


# Si salimos del bucle liberamos la webcam y cerramos las ventanas
cap.release()
cv2.destroyAllWindows()
