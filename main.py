import DetectBarCode
import DetectQR
import DetectFaceEye
import DigitalizeHandWrittenText
import DigitalizeDigitalText
import DetectImage
import cv2

# Establecemos la ruta hasta la imagen a ser analizada
path = "Imagenes/EjemploTodo7.jpg"

# Cargamos la imagen
img = cv2.imread(path)
cv2.imshow("Imagen original", img)
cv2.waitKey(0)


# Llamamos a las funciones

# Obtenemos el texto digitalizado llamando a sus funciones (la primera para texto a mano y la segunda para texto digital)
handwrittenText = DigitalizeHandWrittenText.digitalizeHandWrittenTextFromImage(
    img)
digitalText = DigitalizeDigitalText.digitalizeDigitalTextFromImage(img)

# Detectamos los códigos de barras en la imagen y después mostramos la imagen tras ello
img = DetectBarCode.detectBarCode(img)
cv2.imshow("Imagen tras la detección de código de barras", img)
cv2.waitKey(0)

# Detectamos los códigos QR en la imagen y después mostramos la imagen tras ello
img = DetectQR.detectQR(img)
cv2.imshow("Imagen tras la detección de QR", img)
cv2.waitKey(0)

# Detectamos las sub imágenes en la imagen original y después mostramos la imagen tras ello
img = DetectImage.detectImage(img)
cv2.imshow("Imagen tras la detección de subimagenes", img)
cv2.waitKey(0)

# Detectamos las caras y ojos en la imagen y después mostramos la imagen tras ello
img = DetectFaceEye.detectFaceEyes(img)
cv2.imshow("Imagen tras la detección de caras", img)
cv2.waitKey(0)


# Mostramos la imagen final
cv2.imshow("Imagen", img)

# Mostramos el texto digitalizado
print("Texto a mano digitalizado: ", handwrittenText)
print("Texto en formato digital digitalizado: ", digitalText)
