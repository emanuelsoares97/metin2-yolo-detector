from ultralytics import YOLO
import cv2
import numpy as np
import pyautogui
import time

# 📌 Carregar o modelo treinado
model_path = r"C:\Users\tutas\Documents\Projetos GitHUB\projeto-metin2bot\runs\detect\train\weights\best.pt"
model = YOLO(model_path)  # Carregar o modelo treinado

# 📌 Definir a região de captura (tela inteira ou apenas o jogo)
screen_width, screen_height = pyautogui.size()
capture_region = (0, 0, screen_width, screen_height)  # Captura a tela inteira

# 🎯 Loop para capturar a tela e detectar as Metins
while True:
    # Capturar a tela
    screenshot = pyautogui.screenshot(region=capture_region)
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Converter para o formato OpenCV
    
    # 📌 Realizar a detecção
    results = model(frame)

    # 📌 Processar os resultados e desenhar as caixas de detecção
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas da caixa
            conf = float(box.conf[0])  # Confiança
            cls = int(box.cls[0])
            label = f"{model.names[cls]} {conf:.2f}"

            if conf > 0.2:  # Ajusta o nível de confiança
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 📌 Exibir a detecção ao vivo
    cv2.imshow("Detecção de Metins", frame)

    # Fechar ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 📌 Fechar todas as janelas ao sair
cv2.destroyAllWindows()

