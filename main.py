import pyautogui
import time
import cv2
import numpy as np
import mss

# Lista de templates de Metins (adiciona mais imagens se necessário)
metin_templates = ["metin1.png", "metin2.png"]  # Caminhos das imagens de referência

# Coordenadas da tela do jogo (ajustar conforme necessário)
GAME_REGION = {"left": 283, "top": 107, "width": 1590, "height": 888}  # Ajustado para tua resolução


def capturar_tela():
    """ Captura a tela do jogo e retorna uma imagem do OpenCV """
    with mss.mss() as sct:
        screenshot = sct.grab(GAME_REGION)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)  # Converte para cinza
        return img


def encontrar_metin(img_tela):
    """ Procura por Metins na tela e retorna as coordenadas (x, y) se encontrar """
    melhor_correspondencia = None
    melhor_posicao = None

    for template_path in metin_templates:
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"Erro ao carregar template: {template_path}")
            continue

        res = cv2.matchTemplate(img_tela, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val > 0.7:  # Ajusta o threshold conforme necessário
            print(f"Metin detectada com {max_val * 100:.1f}% de certeza!")
            if melhor_correspondencia is None or max_val > melhor_correspondencia:
                melhor_correspondencia = max_val
                melhor_posicao = max_loc

    if melhor_posicao:
        x, y = melhor_posicao
        print(f"Coordenadas da Metin: ({x}, {y})")
        return x, y
    else:
        print("Nenhuma Metin encontrada.")
        return None


def atacar_metin(posicao):
    """ Move o mouse para a Metin e ataca repetidamente """
    if posicao:
        x, y = posicao
        x += 30  # Ajuste para centralizar melhor
        y += 50  # Ajuste para clicar mais na parte inferior da Metin
        pyautogui.moveTo(x + GAME_REGION["left"], y + GAME_REGION["top"], duration=0.3)
        time.sleep(0.2)
        pyautogui.click()
        print(f"Atacando Metin em ({x}, {y})")

        for _ in range(10):  # Ajuste o número de ataques
            pyautogui.press("space")
            time.sleep(0.3)
    else:
        print("Não foi possível atacar nenhuma Metin.")


def main():
    """ Loop principal do bot """
    while True:
        tela = capturar_tela()
        posicao_metin = encontrar_metin(tela)
        if posicao_metin:
            atacar_metin(posicao_metin)
        else:
            print("Nenhuma Metin visível. Movendo-se...")
            pyautogui.keyDown("w")
            time.sleep(1.5)
            pyautogui.keyUp("w")

        time.sleep(3)  # Tempo entre cada verificação


if __name__ == "__main__":
    print("Bot iniciado! Aguardando...")
    time.sleep(2)
    main()
