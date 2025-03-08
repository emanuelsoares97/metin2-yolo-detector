import pyautogui
import time
import pydirectinput



time.sleep(0.5)


pyautogui.moveTo(1178, 457)

time.sleep(1)
pydirectinput.click()


import pygetwindow as gw
janela = gw.getWindowsWithTitle("Metin2Portugalia")  # Nome da janela do jogo
if janela:
    janela[0].activate()  # Ativa a janela
time.sleep(0.5)  # Pequeno delay para garantir que a janela esteja ativa
pydirectinput.click()
