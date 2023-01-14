# Importamos la librería cv2
import cv2

# Función para detectar códigos QR en una imagen


def detectQR(img):

    # Creamos el detector QR usando cv2
    qcd = cv2.QRCodeDetector()

    # Obtenemos los parámetros de salida de la detección del código QR
    # retval: booleano que indica si se ha detectado o no un código QR
    # decoded_info: info que se obtiene de la lectura del código QR (como la página web a la que se refiere)
    # points: puntos que forman el código QR (sirven para dibujar el rectángulo más tarde)
    # straight_qrcode: imagen del código QR para las celdas en blanco y negro en un array binaria
    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(
        img)

    print("QR Detected:", retval)

    # Contador para guardar las imagenes encontradas
    counter = 0

    # Si se ha detectado un código QR
    if retval:

        # Escribimos la info que se ha obtenido de la lectura del código QR
        for s, p in zip(decoded_info, points):

            # Dibujamos el rectángulo que lo contiene
            img = cv2.polylines(img, points.astype(int), True, (0, 255, 0), 3)
            print("Text in QR:", s)
            # img = cv2.putText(img, s, p[0].astype(int), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            # Cortamos el código de barras detectado y lo guardamos

            QRDetected = img[points[0]
                             [0][1].astype(int):points[0][0][1].astype(int) + (points[0][3][1].astype(int) - points[0][0][1].astype(int)), points[0][0][0].astype(int):points[0][0][0].astype(int) + (points[0][1][0].astype(int) - points[0][0][0].astype(int))]
            print("QR Detected", QRDetected)
            # Mostramos la imagen y la guardamos
            cv2.imwrite('Imagenes/ImagesFromImageDetector/QRDetected' +
                        str(counter) + '.jpg', QRDetected)
            cv2.imshow("QR detected",
                       cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            cv2.waitKey(0)

            # Sumamos uno al contador
            counter = counter + 1

            print("points", points)
            # Ajustamos los puntos del QR detectado para que no se vea el rectangulo verde que resalta al QR
            points[0][0][0] = points[0][0][0] - 5
            points[0][0][1] = points[0][0][1] - 5

            points[0][1][0] = points[0][1][0] + 2
            points[0][1][1] = points[0][1][1] - 5

            points[0][2][0] = points[0][2][0] + 2
            points[0][2][1] = points[0][2][1] + 2

            points[0][3][0] = points[0][3][0] - 5
            points[0][3][1] = points[0][3][1] + 2

            # Ampliamos el área de la imagen para que no se vea cortada
            points = points + 2

            # Una vez le hemos detectado, devolvemos la imagen sin el código de barras (ya que previamente hemos ajustado los puntos del QR detectado)
            img = cv2.fillPoly(img, points.astype(int),
                               (255, 255, 255), cv2.LINE_AA)

    return img

# MAIN


#     # Obtenemos la imagen a leer
# img = cv2.imread('Imagenes/EjemploQR3.png')

# # Llamamos a la función
# detectQR(img)
# cv2.imshow("Image after the QR has been detected", img)
# cv2.waitKey(0)
