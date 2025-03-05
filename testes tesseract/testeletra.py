import pytesseract
import cv2
import numpy as np
import mss
import mss.tools
from time import sleep

sleep(1)

def capturar_tela_jogo():
    with mss.mss() as sct:
        # Captura toda a tela
        tela = sct.grab(sct.monitors[1])  # Monitor principal

        # Converte para um array numpy
        tela = np.array(tela)

        return tela

# Captura a tela do jogo
tela = capturar_tela_jogo()

# Converte para escala de cinza
tela_gray = cv2.cvtColor(tela, cv2.COLOR_RGB2GRAY)

# Aumenta o contraste
tela_gray = cv2.threshold(tela_gray, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Testa OCR
texto = pytesseract.image_to_string(tela_gray)



print("Texto detectado:", texto)

if "Metin" in texto:
    print("Encontrei")