import os
import shutil
import random
import yaml
from util.logger import get_logger

logger=get_logger(__name__)


# Definir caminhos
BASE_DIR = "metin_dataset"
IMAGES_DIR = "metin_images"
LABELS_DIR = "metin_images"

# Criar estrutura de pastas
def criar_pastas():
    for folder in ["images/train", "images/valid", "labels/train", "labels/valid"]:
        os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True)
    logger.info("Pastas criadas com sucesso!")

# Coletar imagens e anotações
def obter_arquivos():
    imagens = [f for f in os.listdir(IMAGES_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]
    anots = [f.replace(os.path.splitext(f)[1], '.txt') for f in imagens]
    return list(zip(imagens, anots))

# Separar em treino (80%) e validação (20%)
def dividir_dados(arquivos):
    random.shuffle(arquivos)
    split = int(0.8 * len(arquivos))
    return arquivos[:split], arquivos[split:]

# Mover arquivos para as pastas corretas
def mover_arquivos(arquivos, tipo):
    for img, txt in arquivos:
        shutil.move(os.path.join(IMAGES_DIR, img), os.path.join(BASE_DIR, f"images/{tipo}", img))
        if os.path.exists(os.path.join(LABELS_DIR, txt)):
            shutil.move(os.path.join(LABELS_DIR, txt), os.path.join(BASE_DIR, f"labels/{tipo}", txt))
    logger.info(f"{tipo.capitalize()} pronto! {len(arquivos)} arquivos movidos.")

# Criar data.yaml
def criar_yaml(classes):
    data = {
        'train': f'./{BASE_DIR}/images/train',
        'val': f'./{BASE_DIR}/images/valid',
        'nc': len(classes),
        'names': classes
    }
    with open(os.path.join(BASE_DIR, "data.yaml"), "w") as f:
        yaml.dump(data, f, default_flow_style=False)
    logger.info("data.yaml criado com sucesso!")

# Carregar classes do arquivo classes.txt
def carregar_classes():
    classes_path = os.path.join(LABELS_DIR, "classes.txt")
    if os.path.exists(classes_path):
        with open(classes_path, "r") as f:
            return [line.strip() for line in f.readlines()]
    else:
        logger.error("ERRO: Arquivo classes.txt não encontrado!")
        return []

if __name__ == "__main__":
    criar_pastas()
    arquivos = obter_arquivos()
    train, valid = dividir_dados(arquivos)
    mover_arquivos(train, "train")
    mover_arquivos(valid, "valid")
    classes = carregar_classes()
    if classes:
        criar_yaml(classes)
    logger.info("Organização do dataset concluída!")
