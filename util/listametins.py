import os
from util.logger import get_logger

imagensLista = get_logger("Lista Imagens")

def get_images_from_folder(folder_path):
    images = []
    if not os.path.exists(folder_path):
        imagensLista.warning(f"The folder {folder_path} does not exist.")
        return images

    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg", ".jpeg")):  # Adiciona suporte a JPEG
            images.append(os.path.join(folder_path, filename))
            imagensLista.info(f"Imagens adicionadas {images}")

    return images

if __name__=="__main__":
    # Caminho da pasta onde as imagens estão armazenadas
    folder_path = './metin_images/'
    metins_imagens = get_images_from_folder(folder_path)

    # Exibe as imagens carregadas
    imagensLista.info(metins_imagens)
