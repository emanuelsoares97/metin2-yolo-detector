import pyautogui
import time
import random
import cv2
import numpy as np

# Configurações iniciais
metins_imagens = ['metin1.png', 'metin2.png', 'metin3.png']  # Caminhos para as imagens dos Metins

def procurar_metins():
    tela = pyautogui.screenshot()
    tela = cv2.cvtColor(np.array(tela), cv2.COLOR_RGB2BGR)
    for metin_imagem in metins_imagens:
        template = cv2.imread(metin_imagem, 0)
        res = cv2.matchTemplate(tela, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.8:
            print(f"Metin {metin_imagem} encontrado!")
            return pyautogui.center((max_loc[0], max_loc[1], template.shape[1], template.shape[0]))
    print("Nenhum metin encontrado.")
    return None

def atacar_metin(posicao):
    if posicao:
        pyautogui.moveTo(posicao)
        for _ in range(10):
            pyautogui.click()
            pyautogui.sleep(0.5)

def mover_inteligentemente():
    # Simples implementação de movimento sistemático
    movimentos = ['w', 'a', 's', 'd']
    for mov in movimentos:
        pyautogui.keyDown(mov)
        time.sleep(1)
        pyautogui.keyUp(mov)

def seguranca():
    if random.randint(1, 100) > 95:
        print("Pausa de segurança ativada.")
        time.sleep(random.uniform(5, 10))  # Pausa aleatória para simular comportamento humano

def main():
    while True:
        seguranca()
        posicao_metin = procurar_metins()
        if posicao_metin:
            atacar_metin(posicao_metin)
        else:
            mover_inteligentemente()
        time.sleep(5)

main()
