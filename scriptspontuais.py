import os

# Diretório onde estão os arquivos de labels
labels_dir = "metin_dataset/labels"

# Percorre as subpastas (train e valid)
for subfolder in ["train", "valid"]:
    path = os.path.join(labels_dir, subfolder)
    
    # Verifica se a pasta existe
    if not os.path.exists(path):
        print(f"Pasta não encontrada: {path}")
        continue
    
    # Processa cada arquivo .txt
    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            file_path = os.path.join(path, filename)

            # Lê o conteúdo original e substitui a classe pela classe 0
            with open(file_path, "r") as file:
                lines = file.readlines()
            
            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) > 0:
                    parts[0] = "0"  # Define a classe como 0
                    new_lines.append(" ".join(parts) + "\n")

            # Escreve o novo conteúdo de volta ao arquivo
            with open(file_path, "w") as file:
                file.writelines(new_lines)

            print(f"✔ Convertido: {filename}")

print("\n🚀 Conversão concluída! Agora todas as Metins são da classe 0.")

