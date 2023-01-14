# Importamos librerías
from pytesseract import pytesseract
import cv2

# Función para digitalizar el text manuscrito de una imagen
# (Se diferencia de la función de digitalizar texto digital porque esta función
#  aplica más filtros a la imagen para adaptarla mejor al OCR y mejorar la precisión)


def digitalizeHandWrittenTextFromImage(img):

    # Establecemos el path a tesseract.exe
    path_to_tesseract = r'C:/Users/jesus/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'

    # Hacemos que la cmd de pytesseract use el path a tesseract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    # Comprobamos que la imagen es válida
    if img is None:
        print("No se ha encontrado nada en la imagen o la imagen no existe")
        return

    # Convertimos la imagen a escala de grises
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicamos un filtro a la imagen para desenfocarla
    img = cv2.blur(img, (10, 10))

    # Aplicamos thresholding para convertir la imagen
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Ejecutamos el OCR para obtener el texto de la imagen
    text = pytesseract.image_to_string(img)

    # Mostramos el texto por consola
    print(text)

    return text


# MAIN

# # Cargamos la imagen
# img = cv2.imread("Imagenes/EjemploAMano11.png")

# # Llamamos a la función
# digitalizeHandWrittenTextFromImage(img)
