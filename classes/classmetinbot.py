from ultralytics import YOLO
import cv2
import numpy as np
import pyautogui
import time

from util.logger import get_logger

MetinBotLogger = get_logger("MainLogger")

class MetinBot:
    def __init__(self, model_path="models/best.pt"):
        """
        Inicializa o bot carregando o modelo treinado.
        """
        self.model = YOLO(model_path)
        self.capture_region = (0, 0, *pyautogui.size())  # Captura tela inteira
        MetinBotLogger.info(f"Bot iniciado com modelo: {model_path}")

    def capturar_tela(self):
        """
        Captura a tela e converte para formato OpenCV.
        """
        try:
            screenshot = pyautogui.screenshot(region=self.capture_region)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Converter para o OpenCV
            return frame
        except Exception as e:
            MetinBotLogger.error(f"Erro ao capturar tela: {e}")
            return None

    def detectar_metins(self, frame):
        """
        Realiza a detecção de Metins na imagem capturada.
        """
        try:
            results = self.model(frame)
            MetinBotLogger.info(f"Detecção realizada com sucesso.")
            return results
        except Exception as e:
            MetinBotLogger.error(f"Erro na detecção: {e}")
            return []

    def processar_deteccoes(self, frame, results):
        """
        Processa os resultados da detecção e desenha caixas ao redor dos Metins.
        """
        try:
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas da caixa
                    conf = float(box.conf[0])  # Confiança
                    cls = int(box.cls[0])
                    label = f"{self.model.names[cls]} {conf:.2f}"

                    if conf > 0.2:  # Confiança mínima para exibir
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            return frame
        except Exception as e:
            MetinBotLogger.error(f"Erro ao processar detecções: {e}")
            return frame

    def iniciar(self):
        """
        Inicia o loop de captura e detecção em tempo real.
        """
        MetinBotLogger.info("Bot em execução...")
        while True:
            frame = self.capturar_tela()
            if frame is None:
                continue

            results = self.detectar_metins(frame)
            frame = self.processar_deteccoes(frame, results)

            cv2.imshow("Detecção de Metins", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
        MetinBotLogger.info("Bot encerrado.")


if __name__ == "__main__":
    bot = MetinBot()
    bot.iniciar()
