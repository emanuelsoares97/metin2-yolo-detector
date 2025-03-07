import pyautogui
import time
import os

def capture_screenshots(interval, duration, save_path):
    """
    Captura screenshots automaticamente.
    
    Args:
    interval (float): Intervalo em segundos entre cada screenshot.
    duration (float): Duração total em segundos para capturar screenshots.
    save_path (str): Caminho onde os screenshots serão salvos.
    """
    start_time = time.time()
    counter = 374
    
    # Cria o diretório de destino se não existir
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    while (time.time() - start_time) < duration:
        # Captura a screenshot
        screenshot = pyautogui.screenshot()
        # Define o nome do arquivo
        file_name = f"metin_{counter}.png"
        # Salva a screenshot no caminho especificado
        screenshot.save(os.path.join(save_path, file_name))
        print(f"Screenshot {counter} salva em {os.path.join(save_path, file_name)}")
        counter += 1
        # Espera o intervalo especificado antes da próxima captura
        time.sleep(interval)

# Configuração do usuário
intervalo = 5  # segundos entre cada screenshot
duracao = 300  # segundos totais para capturar (5 minutos)
caminho_para_salvar = 'C:/Users/tutas/Documents/Projetos GitHUB/projeto-metin2bot/metin_images'

# Chamada da função
capture_screenshots(intervalo, duracao, caminho_para_salvar)
