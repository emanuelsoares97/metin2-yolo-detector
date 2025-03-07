import yaml

# Caminho do diretório do dataset
dataset_path = "metin_dataset"

# Defina os caminhos para treino e validação
data = {
    "train": f"{dataset_path}/images/train",  
    "val": f"{dataset_path}/images/valid",   
    "nc": 3,  # Número de classes (ajuste conforme necessário)
    "names": ["Metin_Sombra", "Metin_Escuridao", "Metin_Ciume"]  # Substitua pelos nomes reais das classes
}

# Salvar o arquivo
with open(f"{dataset_path}/data.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)

print("✔ Arquivo data.yaml gerado com sucesso!")
