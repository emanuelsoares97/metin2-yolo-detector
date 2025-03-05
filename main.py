import pyautogui
import pytesseract
import numpy as np
import cv2
import time
import random
from util.logger import get_logger

mainLogger = get_logger("Main Logger")

# Configuração do Tesseract OCR (mude o caminho se necessário)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def procurar_metins():
    tela = pyautogui.screenshot()
    tela = np.array(tela)

    # Definir uma região de interesse (ROI) onde os nomes das Metins costumam aparecer
    altura, largura, _ = tela.shape
    roi = tela[0:int(altura * 0.5), :]  # Pegamos só a metade superior da tela

    # Converter para escala de cinza
    tela_gray = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)

    # Melhorar contraste e nitidez para o OCR
    tela_gray = cv2.threshold(tela_gray, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    from pytesseract import image_to_string
    print(image_to_string(tela_gray))


    # OCR apenas na área recortada
    texto_detectado = pytesseract.image_to_data(tela_gray, output_type=pytesseract.Output.DICT)

    # Ajustes para mover o clique corretamente para a pedra Metin
    OFFSET_X = 20  # Ajuste para mover mais para a direita
    OFFSET_Y = 70  # Ajuste para descer mais

    for i, palavra in enumerate(texto_detectado["text"]):
        if "Metin" in palavra:
            x = texto_detectado["left"][i]  # Coordenada X da palavra "Metin"
            y = texto_detectado["top"][i]   # Coordenada Y da palavra "Metin"
            largura = texto_detectado["width"][i]
            altura = texto_detectado["height"][i]

            # Como recortamos a parte superior da tela, precisamos ajustar Y de volta para a posição original
            y += int(altura * 0.5)

            # Calcula o centro do nome "Metin"
            x_centro = x + largura // 2 + OFFSET_X  # Move um pouco para a direita
            y_centro = y + altura // 2 + OFFSET_Y   # Move mais para baixo

            print(f"Metin detectada! Nova posição ajustada: ({x_centro}, {y_centro})")
            return (x_centro, y_centro)

    print("Nenhuma Metin encontrada via OCR.")
    return None





def atacar_metin(posicao):
    if posicao:
        x, y = posicao
        print(f"Movendo para a Metin na posição OCR: ({x}, {y})")

        # Move lentamente para garantir precisão no clique
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(0.2)

        pyautogui.click()  # Clica na palavra "Metin"
        print(f"Clicando na Metin em ({x}, {y})")

        # Simula ataques repetidos (pressionando espaço)
        for _ in range(10):  
            pyautogui.press("space")  # Ajuste se a tecla de ataque for diferente
            time.sleep(0.3)

        print("Atacando Metin...")
    else:
        print("Não foi possível atacar nenhuma Metin.")


def mover_inteligentemente():
    # Movimentação aleatória caso não encontre uma Metin
    movimentos = ['w', 'a', 's', 'd']
    for mov in movimentos:
        pyautogui.keyDown(mov)
        time.sleep(1)
        pyautogui.keyUp(mov)


def seguranca():
    if random.randint(1, 100) > 95:
        mainLogger.info("⏸️ Pausa de segurança ativada.")
        time.sleep(random.uniform(3, 5))


def main():
    time.sleep(2)
    while True:
        posicao_metin = procurar_metins()
        if posicao_metin:  # Agora posicao_metin é (x, y), não apenas True
            atacar_metin(posicao_metin)
        else:
            mover_inteligentemente()
        time.sleep(5)


if __name__ == "__main__":
    time.sleep(2)
    mainLogger.info("🚀 Bot iniciado!")
    main()
