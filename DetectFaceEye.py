# Importamos librerías
import cv2

# Función para detectar caras y ojos en una imagen


def detectFaceEyes(img):

    # Cargar el clasificador entrenado "Haar Cascade" para las caras desde el fichero XML
    haar_face_cascade = cv2.CascadeClassifier(
        'opencv/data/haarcascade_frontalface_alt.xml')

    # Cargar el clasificador entrenado "Haar Cascade" para los ojos desde el fichero XML
    haar_eyes_cascade = cv2.CascadeClassifier(
        'opencv/data/haarcascade_eye_tree_eyeglasses.xml')

    # Pasamos la imagen a blanco y negro
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Buscar las caras en la imagen y devolver las posiciones detectadas con un rectángulo(x, y, w, h)
    faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.2,
                                               minNeighbors=5)

    # Devolver el número de caras detectadas en la imagen
    print('Caras encontradas: ', len(faces))

    # Si encontramos caras
    if len(faces) > 0:

        # Crear los rectangulos de las caras
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # Buscar los ojos en la imagen y devolver las posiciones detectadas con un rectángulo(x, y, w, h)
        eyes = haar_eyes_cascade.detectMultiScale(gray_img)

        # Devolver el número de ojos detectados en la imagen
        print('Ojos encontrados: ', len(eyes))

        # Crear los rectangulos de los ojos
        for (x, y, w, h) in eyes:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    else:
        print('No se han encontrado caras en la imagen')

    return img


# MAIN


# Obtenemos la imagen a leer
# img = cv2.imread('Imagenes/EjemploTodo3.png')

# # Mostrar la imagen original
# cv2.imshow('Imagen original', img)
# cv2.waitKey(0)

# # Llamamos a la función
# detectFaceEyes(img)

# # Mostrar la imagen con los ojos y caras detectadas
# cv2.imshow('Imagen con las caras y ojos detectados', img)
# cv2.waitKey(0)
