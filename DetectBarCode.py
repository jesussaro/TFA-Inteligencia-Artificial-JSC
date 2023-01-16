# Importamos la librería pyzbar y cv2
from pyzbar import pyzbar
import cv2
from PIL import Image

# Función para detectar códigos de barras en una imagen


def detectBarCode(img):

    # Ejecutamos el detector de códigos de barras de la librería pyzbar
    detectedBarCode = pyzbar.decode(img)

    # Contador para guardar las imagenes encontradas
    counter = 0

    # Comprobamos que se ha detectado algún código
    if detectedBarCode:
        print("Bar code Detected: true")
        # Recorremos todos los códigos detectados
        for detectedBarCode in detectedBarCode:
            # Obtenemos las dimensiones y coordenadas del código de barras detectado en la imagen
            x, y, w, h = detectedBarCode.rect
            # Imprimimos en la imagen un rectángulo verde para marcar el código de barras detectado
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Obtenemos la información / redirección del código de barras y la imprimimos en la imagen
            dataInside = detectedBarCode.data.decode("utf-8")
            print("Text in barcode:", dataInside)

            # Cortamos el código de barras detectado y lo guardamos
            barCodeDetected = img[y:y+h, x:x+w]

            # Mostramos la imagen y la guardamos
            cv2.imwrite('Imagenes/ImagesFromImageDetector/BarCodeDetected' +
                        str(counter) + '.jpg', barCodeDetected)
            cv2.imshow("Bar code detected", barCodeDetected)
            cv2.waitKey(0)

            # Sumamos uno al contador para que se guarde con otro nombre la imagen con el código de barras detectado
            counter = counter + 1

            # Una vez le hemos detectado, devolvemos la imagen sin el código de barras
            cv2.rectangle(img, (x - 2, y - 2), (x+w + 2, y+h + 2),
                          (255, 255, 255), -1)

    else:
        # Si no se ha detectado ningún código de barras, se muestra este mensaje
        print("Bar code Detected: false")
    # Devolvemos la imagen
    return img


# MAIN

# Obtenemos la imagen a leer
# img = cv2.imread('Imagenes/EjemploTodo5.png')
# cv2.imshow("Original Image", img)
# cv2.waitKey(0)

# # Llamamos a la función
# detectBarCode(img)
# cv2.imshow("Image after the bar code has been detected", img)
# cv2.waitKey(0)
