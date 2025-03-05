import pyautogui
import time

print("Move o mouse para os cantos da janela do jogo e aguarda...")

for i in range(5):  # Tempo para posicionar
    print(f"Aguarda {5-i} segundos...")
    time.sleep(1)

# Pega a posição atual do mouse (onde o canto superior esquerdo do jogo deve estar)
x1, y1 = pyautogui.position()
print(f"Canto superior esquerdo detectado em: ({x1}, {y1})")

print("\nAgora move o mouse para o canto inferior direito do jogo e aguarda...")

for i in range(5):
    print(f"Aguarda {5-i} segundos...")
    time.sleep(1)

# Pega a posição final do mouse (onde o canto inferior direito do jogo deve estar)
x2, y2 = pyautogui.position()
print(f"Canto inferior direito detectado em: ({x2}, {y2})")

print("\nAgora temos as coordenadas exatas da janela do jogo!")
print(f"Recorte do jogo -> Top Left: ({x1}, {y1}), Bottom Right: ({x2}, {y2})")
