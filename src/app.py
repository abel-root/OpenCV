import numpy as np
import cv2 as cv

# Ouvrir la caméra
captObj = cv.VideoCapture(0)
assert captObj.isOpened(), "Impossible d'ouvrir la caméra."

# Paramètres vidéo
frame_width = int(captObj.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(captObj.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = 30
fourcc = cv.VideoWriter_fourcc(*'mp4v') # type: ignore
writeObj = cv.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

# Capture avec affichage
while True:
    isFrameReturned, img = captObj.read()
    if not isFrameReturned:
        break

    writeObj.write(img)  # Enregistrer la frame
    cv.imshow("Capture en direct", img)  # Affichage en temps réel

    # Appuyer sur 'q' pour quitter
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Libération
captObj.release()
writeObj.release()
cv.destroyAllWindows()
