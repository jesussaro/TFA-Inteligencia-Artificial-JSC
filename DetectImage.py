# Importamos la librería cv2
import cv2

# Función para detectar sub imagenes en una imagen


def detectImage(img):

    # Convertimos la imagen a blanco y negro
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Obtengo la anchura, altura y profundidad de la imagen
    height, width, channels = img.shape

    # Aplicamos un umbral a la imagen para convertirla en binaria
    ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

    # Encuentra los contornos de la imagen
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Contador para guardar las imagenes encontradas
    counter = 0

    # Recorre todos los contornos
    for c in contours:
        # Obtiene las coordenadas del rectángulo que encierra el contorno
        x, y, w, h = cv2.boundingRect(c)

        # Calcula el área del rectángulo y del contorno
        area_rect = w * h
        area_contour = cv2.contourArea(c)

        # Si el área de la sub imagen encontrada es mayor que el 20% de la imagen original y menor que el 99% de la imagen original, la aceptamos
        # Esto se hace para que no detecte imagenes demasiado pequeñas o demasiado grandes, un filtro
        if area_rect > ((0.2*height)*(0.2*width)) and area_rect < ((0.99*height)*(0.99*width)):
            # Recorta la sub imagen encontrada
            imageDetected = img[y:y+h, x:x+w]
            # La mostramos y la guardamos
            cv2.imshow("ImageDetected " +
                       str(counter), imageDetected)
            cv2.waitKey(0)
            # Guardamos la imagen con el nombre ImageDetected.jpg pero con un contador para que no se sobreescriba en el caso de que haya más de una sub imagen
            cv2.imwrite('Imagenes/ImagesFromImageDetector/ImageDetected' +
                        str(counter) + '.jpg', imageDetected)

            # Dibuja un rectángulo alrededor del contorno
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # Aumentamos el contador para guardar la siguiente sub imagen
            counter = counter + 1
    # Devolvemos la imagen original con los rectángulos recalcando la sub imagen encontrada
    return img

# MAIN


# Obtenemos la imagen a leer
img = cv2.imread('Imagenes/EjemploDeteccionImagen3.png')
# La mostramos
cv2.imshow('Original image', img)
cv2.waitKey(0)

# Llamamos a la función
detectImage(img)
# Muestra la imagen original con los rectángulos recalcando la sub imagen encontrada
cv2.imshow('Final result', img)
cv2.waitKey(0)
