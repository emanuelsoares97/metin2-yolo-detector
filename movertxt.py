import os
import shutil

# Caminhos das pastas
IMAGES_DIR = "metin_images"
LABELS_DIR = "metin_dataset/labels"
TRAIN_IMAGES_DIR = "metin_dataset/images/train"
VALID_IMAGES_DIR = "metin_dataset/images/valid"

# Criar estrutura se não existir
os.makedirs(os.path.join(LABELS_DIR, "train"), exist_ok=True)
os.makedirs(os.path.join(LABELS_DIR, "valid"), exist_ok=True)

# Ver quais imagens estão no treino e validação
train_images = set(os.listdir(TRAIN_IMAGES_DIR))
valid_images = set(os.listdir(VALID_IMAGES_DIR))

# Mover os arquivos de anotação correspondentes
for file in os.listdir(IMAGES_DIR):
    if file.endswith(".txt"):
        image_file = file.replace(".txt", ".png")  # Ajuste se suas imagens forem .jpg
        if image_file in train_images:
            shutil.move(os.path.join(IMAGES_DIR, file), os.path.join(LABELS_DIR, "train", file))
        elif image_file in valid_images:
            shutil.move(os.path.join(IMAGES_DIR, file), os.path.join(LABELS_DIR, "valid", file))

print("✔ Arquivos .txt movidos para as pastas corretas!")
