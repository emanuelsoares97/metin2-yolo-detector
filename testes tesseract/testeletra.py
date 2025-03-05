import mss
import numpy as np
import cv2
import pytesseract

# 📌 COORDENADAS DA JANELA DO JOGO (ajustadas manualmente)
x1, y1 = 283, 107   # Canto superior esquerdo
x2, y2 = 1873, 995  # Canto inferior direito

def capturar_texto():
    with mss.mss() as sct:
        monitor = {
            "top": y1,
            "left": x1,
            "width": x2 - x1,
            "height": y2 - y1
        }
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)

        # 🔹 Converte para escala de cinza
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 🔹 Suavização para reduzir ruídos
        img_gray = cv2.GaussianBlur(img_gray, (3, 3), 0)

        # 🔹 Ajuste de brilho e contraste (mais suave)
        alpha = 1.1  # 🔽 Reduzimos o contraste para evitar distorção
        beta = 15    # 🔽 Aumentamos o brilho apenas um pouco
        img_gray = cv2.convertScaleAbs(img_gray, alpha=alpha, beta=beta)

        # 🔹 Testar sem threshold primeiro
        return img_gray

# 🔹 Captura a imagem processada
imagem_processada = capturar_texto()

# 🔹 Salva para debug (ver como está antes do OCR)
cv2.imwrite("debug_janela_suave.png", imagem_processada)

# 🔹 Configuração do OCR (melhor para texto em linha)
custom_config = r'--oem 3 --psm 7'  
texto = pytesseract.image_to_string(imagem_processada, config=custom_config, lang="eng")

print("Texto detectado:", texto)




if "Metin" in texto:
    print("Encontrei")

