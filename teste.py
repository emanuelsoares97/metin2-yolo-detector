import ctypes
from time import sleep
def clicar_mouse(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)  # Move o cursor para a posição
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # Pressiona botão esquerdo
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # Solta botão esquerdo

sleep(1)
clicar_mouse(1321,375)












