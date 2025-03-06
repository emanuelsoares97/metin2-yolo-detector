# 📌 Metin2 Bot - Automacao para Deteccao de Metins com Machine Learning

## 📖 **Descricao do Projeto**
Este projeto tem como objetivo automatizar a **detecção das Metins** no jogo **Metin2**. Utilizando **Machine Learning** com a arquitetura **YOLO (You Only Look Once)**, o bot consegue identificar as Metins na tela de forma precisa e eficiente.

Inicialmente, testamos abordagens como **cor, OCR (Reconhecimento de Texto) e Template Matching**, mas essas apresentaram limitações, como:
- **Sensibilidade a mudanças de iluminacao**
- **Detecção falha em certos angulos**
- **Erros ao capturar Metins em diferentes mapas**

Por isso, decidimos treinar um modelo **YOLOv8** especializado para reconhecer as Metins de forma robusta e sem necessidade de ajustes manuais constantes.

---

## 🛠️ **Etapas do Desenvolvimento**

### 🔹 1. **Tentativas Iniciais**
- **Template Matching (OpenCV)**: Comparacao com imagens de referencia.
- **OCR (pytesseract)**: Identificacao da palavra "Metin" na tela.
- **Filtros de Imagem**: Aplicacao de filtros para melhorar a deteccao.
- **Problema**: Essas abordagens falharam devido a iluminacao, posicoes variaveis e diferentes tipos de Metins no jogo.

### 🔹 2. **Implementacao do Machine Learning com YOLO**
- **Coleta e rotulacao de imagens**: Capturamos e anotamos manualmente as Metins.
- **Treinamento do modelo YOLOv8**:
  - Ajustamos para detectar **todas as Metins** independentemente da cor ou mapa.
  - Reduzimos o modelo para identificar apenas **uma classe genérica de Metins**, aumentando a precisao.
- **Testes e ajustes**:
  - Corrigimos erros de detecção incorreta.
  - Aumentamos o numero de imagens para melhorar o aprendizado.
  - Refinamos a precisao do modelo com mais epocas de treino.

---

## 🔍 **Status Atual do Projeto**
Atualmente, o bot já consegue:
✅ **Identificar Metins com alta precisao**
✅ **Independer da cor ou tipo da Metin**
✅ **Ser treinado e melhorado facilmente**
✅ **Executar o reconhecimento em tempo real**

Estamos agora ajustando pequenos detalhes e otimizando o modelo para melhor desempenho.

---

## 🚀 **Como Executar o Projeto**
1. **Instale as dependencias**:
   ```sh
   pip install -r requirements.txt
   ```
2. **Ative o ambiente virtual**:
   ```sh
   source venv/bin/activate   # Linux/macOS
   .\venv\Scripts\activate  # Windows
   ```
3. **Execute o bot**:
   ```sh
   python main.py
   ```

---

## 🔧 **Tecnologias Utilizadas**
- **Python**
- **YOLOv8 (Ultralytics)**
- **OpenCV** (processamento de imagem)
- **mss** (captura de tela)
- **PyAutoGUI** (automacao do mouse e teclado)

---

## 📌 **Conclusao**
O projeto evoluiu significativamente desde as abordagens iniciais até a implementação do **YOLOv8** para reconhecimento de Metins. Agora, o bot é muito mais preciso e eficiente.

📢 **Proximos passos: Melhorar o desempenho e testar em diferentes ambientes do jogo!** 🚀

