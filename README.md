# 📌 Metin2Bot - Detector de Metins com YOLOv8

Este projeto é um bot para detecção de Metins no jogo Metin2, utilizando **YOLOv8** para identificar pedras Metin no mapa e auxiliar no farm automatizado.

---
## 📁 Estrutura do Projeto
```
projeto-metin2bot/
│── metin_dataset/          # Contém as imagens e anotações do dataset (não subir para o GitHub)
│   ├── images/             # Pasta com imagens de treino e validação
│   ├── labels/             # Anotações do YOLO para cada imagem
│   ├── data.yaml           # Arquivo de configuração do dataset
│
│── runs/                   # Resultados dos treinamentos do YOLO (não subir)
│
│── scripts/                # Scripts Python para treino, predição e automação do bot
│   ├── train.py            # Script para treinar o modelo
│   ├── detect.py           # Script para fazer predições
│   ├── utils.py            # Funções auxiliares
│
│── models/                 # Pesos do modelo treinado (baixar antes de rodar)
│   ├── best.pt             # Melhor modelo treinado
│   ├── last.pt             # Último modelo salvo
│
│── requirements.txt        # Dependências do projeto
│── .gitignore              # Arquivos a serem ignorados no Git
│── README.md               # Documentação do projeto
│── main.py                 # Arquivo principal que roda o bot
│── config.yaml             # Configurações gerais do projeto
```

---
## 🔧 **Configuração do Ambiente**

### 1️⃣ **Clonar o repositório**
```bash
git clone https://github.com/emanuelsoares97/projeto-metin2bot.git
cd projeto-metin2bot
```

### 2️⃣ **Criar e ativar o ambiente virtual**
```bash
python -m venv venv
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate
```

### 3️⃣ **Instalar as dependências**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Baixar os pesos do modelo**
Baixe o arquivo `best.pt` do YOLOv8 treinado e coloque na pasta `models/`.

📥 **Baixar modelo:** [Em breve, link aqui]

---
## 🚀 **Como Usar**

### 🔍 **Fazer predição em uma imagem**
```bash
python scripts/detect.py --model models/best.pt --source caminho/para/imagem.png
```

### 🏋️ **Treinar um novo modelo**
```bash
python scripts/train.py --epochs 100 --img-size 800
```

---
## 🛠 **Customização**
- **Ajustar limiar de confiança**: Modifique `conf=0.2` no script de predição para calibrar a detecção.
- **Alterar dataset**: Adicione mais imagens em `metin_dataset/` e ajuste `data.yaml`.

---
## 📌 **Contribuição**
Sinta-se à vontade para abrir **issues** ou enviar **pull requests** para melhorias!

---
## ⚠️ **Atenção**
Este projeto é um estudo de automação e detecção de objetos, sem fins lucrativos. Use com responsabilidade.

---
## 📞 **Contato**
📧 Email: _[seuemail@exemplo.com]_  
💬 Discord: _[SeuUsuário#1234]_


