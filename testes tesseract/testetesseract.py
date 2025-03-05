import pyautogui
import cv2
import numpy as np
import pytesseract
from time import sleep

sleep(2)

# Captura a tela e salva como imagem
tela = pyautogui.screenshot()
tela = np.array(tela)
cv2.imwrite("screenshot_test.png", tela)

# Converte para escala de cinza
tela_gray = cv2.cvtColor(tela, cv2.COLOR_RGB2GRAY)
cv2.imwrite("screenshot_gray.png", tela_gray)

# Aplica um ajuste no contraste
tela_gray = cv2.threshold(tela_gray, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imwrite("screenshot_contraste.png", tela_gray)

# Testar o que o OCR está lendo
print("Texto detectado:")
print(pytesseract.image_to_string(tela_gray))
