import os
from util.logger import get_logger

logger= get_logger(__name__)

# Caminho da pasta onde os arquivos estão
pasta = "metin2_images"
pasta = os.path.join(pasta, "metin2_images")

# Percorre todos os arquivos na pasta
for arquivo in os.listdir(pasta):
    if arquivo.endswith(".xml"):  # Se o arquivo terminar com .xml
        novo_nome = arquivo.replace(".xml", ".txt")  # Troca .xml por .txt
        os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_nome))
        logger.info(f"Renomeado: {arquivo} -> {novo_nome}")
