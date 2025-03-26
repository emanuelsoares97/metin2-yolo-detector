# Metin2 Bot - Detector de Metins com YOLOv8 + OpenCV

Este é um bot para **detecção automática de pedras Metin** no jogo **Metin2**, utilizando **YOLOv8** e **OpenCV**.

Embora o sistema de clique automático **não tenha sido implementado** (por depender de Arduino ou outras soluções físicas), a **detecção em tempo real está totalmente funcional**, com ótimos resultados de precisão.

---

## Estrutura do Projeto

```
projeto-metin2bot/
│── classes/
│   ├── classemetinbot.py
│── logs/
│── models/
│   ├── best.pt           # Modelo treinado
│   ├── yolov8n.pt        # Modelo base do YOLO
│── runs/                 # Resultados do treino
│── util/ # funçoes auxiliares
│── main.py               # Script principal
│── requirements.txt
│── .gitignore
│── LICENSE
│── README.md
```

---

## Instalação

### **Criar e ativar um ambiente virtual**
```bash
python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### **Instalar as dependências**
```bash
pip install -r requirements.txt
```

---

## Como Usar o Bot

### **Rodar a detecção**
```bash
python main.py
```

O script irá abrir a tela de jogo e começar a detectar as pedras Metin.

### **2Parar o bot**
Pressione **`Q`** para sair.

---

## Resultados do Modelo

O modelo YOLOv8 foi treinado com 100 epochs e atingiu ótimos resultados:

- `mAP50 ≈ 0.9` (alta precisão)
- `Precision ≈ 0.85`
- `Recall ≈ 0.85`


---

## Treinar um Novo Modelo

Se quiser treinar seu próprio modelo usando suas imagens:

```bash
yolo task=detect mode=train model=yolov8n.pt data=metin_dataset/data.yaml epochs=100 imgsz=800
```

O melhor modelo será guardado em:
```
models/best.pt
```

---

## Tecnologias Utilizadas

- **YOLOv8 (Ultralytics)** — detecção
- **OpenCV** — captura e manipulação da tela
- **LabelImg** — ferramenta usada para anotar as imagens (bounding boxes)
- **PyTorch** — backend do YOLO
- **PyAutoGUI** *(testado)* — tentativa de automação dos cliques (sem sucesso no Metin2)
- **Pynput** *(testado)* — tentativa de controle do teclado/mouse
- **Logger customizado**

---

## Melhorias Futuras

- Adicionar movimento automático do personagem
- Implementar clique automático com Arduino

---

## Licença

Este projeto está sob a **Licença MIT**. Sinta-se à vontade para usar, estudar e evoluir o bot!

---

## Contato

Dúvidas ou sugestões?  
Entre em contato comigo no GitHub: [emanuelsoares97](https://github.com/emanuelsoares97)

---

**Boas caçadas de Metins!**  
**Aprendizado aplicado à prática com visão computacional!**
