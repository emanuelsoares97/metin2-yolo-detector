from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
from util.logger import get_logger

imagensSite = get_logger("ModuloImagensSite")

def download_images(url, folder_path='./metin_images/'):
    navegador = None
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            imagensSite.info(f"Pasta criada: {folder_path}")

        navegador = webdriver.Chrome()
        imagensSite.info("Navegador iniciado.")

        navegador.get(url)
        imagensSite.info("URL acessada.")

        navegador.implicitly_wait(10)
        imagensSite.info("Aguardando o carregamento completo da página.")

        html_content = navegador.page_source
        imagensSite.info("Conteúdo HTML obtido.")

        soup = BeautifulSoup(html_content, 'html.parser')
        imagensSite.info("Análise do HTML realizada.")

        images = soup.find_all('img', src=lambda src: src and 'Metin' in src)
        imagensSite.info(f"{len(images)} imagens encontradas para download.")

        for img in images:
            image_url = img['src']
            if not image_url.startswith(('http:', 'https:')):
                image_url = 'https://wiki.mt2portugalia.pt' + image_url
            
            image_name = image_url.split('/')[-1]
            img_data = requests.get(image_url).content
            with open(os.path.join(folder_path, image_name), 'wb') as file:
                file.write(img_data)
            imagensSite.info(f"Download concluído: {image_name}")
    
    except Exception as e:
        imagensSite.error(f"Erro durante o download das imagens: {e}")
    finally:
        if navegador:
            navegador.quit()
            imagensSite.info("Navegador fechado.")

if __name__ == "__main__":
    wiki_url = 'https://wiki.mt2portugalia.pt/index.php?title=Metins'
    download_images(wiki_url)
    imagensSite.info("Processo de download das imagens concluído.")
