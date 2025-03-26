import os
from util.logger import get_logger

logger= get_logger(__name__)

# Caminho da pasta onde os arquivos estão
pasta = "C:/Users/tutas/Documents/Projetos GitHUB/projeto-metin2bot/metin_images"  # Atualize com o caminho correto

# Percorre todos os arquivos na pasta
for arquivo in os.listdir(pasta):
    if arquivo.endswith(".xml"):  # Se o arquivo terminar com .xml
        novo_nome = arquivo.replace(".xml", ".txt")  # Troca .xml por .txt
        os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))
        logger.info(f"Renomeado: {arquivo} -> {novo_nome}")
