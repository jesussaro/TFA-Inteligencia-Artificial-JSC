# Importamos librerías
from pytesseract import pytesseract
import cv2

# Función para digitalizar el texto (digital o manuscrito) de una imagen


def digitalizeDigitalTextFromImage(img):

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

    # Ejecutamos el OCR para obtener el texto de la imagen
    text = pytesseract.image_to_string(img)

    # Mostramos el texto por consola
    print(text)

    return text


# MAIN

# # Cargamos la imagen
# img = cv2.imread("Imagenes/EjemploTodo5.png")

# # Llamamos a la función
# digitalizeDigitalTextFromImage(img)
