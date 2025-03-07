# Metin2 Bot - Detector de Metins com YOLOv8 🚀

Este é um bot para **detecção automática de Metins** no jogo **Metin2** utilizando **YOLOv8** e **OpenCV**.

---

## 📌 Estrutura do Projeto

```
projeto-metin2bot/
│── classes/
│   ├── classemetinbot.py
│── logs/
│── metin_dataset/  # Base de dados do YOLO (IGNORADO no Git)
│── metin_images/
│── models/
│   ├── best.pt  # Modelo treinado
│   ├── yolov8n.pt  # Modelo base do YOLO
│── runs/
│── util/
│   ├── logger.py  # Gerenciador de logs
│── main.py 
│── requirements.txt
│── .gitignore
│── LICENSE
│── README.md

```

---

## ⚡ Instalação

### **1️⃣ Criar e ativar um ambiente virtual**
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### **2️⃣ Instalar as dependências**
```sh
pip install -r requirements.txt
```

---

## 🎯 Como Usar o Bot

### **1️⃣ Rodar a detecção ao vivo**
```sh
python main.py
```

Isso iniciará a detecção de Metins na tela.

### **2️⃣ Parar o bot**
Pressione **`Q`** para sair.

---

## 🛠️ Como Treinar um Novo Modelo
Se quiser treinar um novo modelo com YOLOv8:

```sh
yolo task=detect mode=train model=yolov8n.pt data=metin_dataset/data.yaml epochs=100 imgsz=800
```

Após o treinamento, o melhor modelo será salvo em:
```
models/best.pt
```

---

## 📌 Melhorias Futuras
- ✅ Melhorar a precisão do modelo
- ✅ Automatizar a movimentação do personagem
- ✅ Criar um sistema de auto-ataque

---

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar!

---

## 📬 Contato
Caso tenha dúvidas ou sugestões, entre em contato: **emanuelsoares97** no GitHub.

---

🚀 **Boas caçadas de Metins!** 🎯

