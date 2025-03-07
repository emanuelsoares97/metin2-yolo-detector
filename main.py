from ultralytics import YOLO
import cv2
import numpy as np
import pyautogui
import time

from util.logger import get_logger

MainLogger= get_logger("MainLogger")

# Carregar o modelo treinado
model_path = r"models/best.pt"
model = YOLO(model_path)  # Carregar o modelo treinado
MainLogger.info(f"Bot carregado: {model}")

# captura monitor inteiro
screen_width, screen_height = pyautogui.size()
capture_region = (0, 0, screen_width, screen_height)
MainLogger.info(f"Captura do monitor iniciada.")

# Loop para capturar a tela e detectar as Metins
while True:
    MainLogger.info("Bot iniciado.")
    try:
        # Capturar a tela
        screenshot = pyautogui.screenshot(region=capture_region)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Converter para o formato OpenCV
        
        # Realizar a detecção
        results = model(frame)

        # Processar os resultados e desenhar as caixas de detecção
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas da caixa
                conf = float(box.conf[0])  # Confiança
                cls = int(box.cls[0])
                label = f"{model.names[cls]} {conf:.2f}"

                if conf > 0.2:  # Ajusta o nível de confiança
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Exibir a detecção
        cv2.imshow("Detecção de Metins", frame)

        # Fechar o bot no "q"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        MainLogger.error(f"Tentativa de rodar bot falhada, erro: {e}")

#Fechar todas as janelas ao sair
cv2.destroyAllWindows()

