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
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Converter para OpenCV
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

    def encontrar_metin_mais_proxima(self, results):
        """
        Encontra a Metin mais próxima para atacar.
        """
        metins = []

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas da caixa
                conf = float(box.conf[0])  # Confiança

                if conf > 0.2:  # Apenas considerar se a detecção for confiável
                    centro_x = (x1 + x2) // 2
                    centro_y = (y1 + y2) // 2
                    metins.append((centro_x, centro_y))

        if metins:
            return sorted(metins, key=lambda p: p[0] ** 2 + p[1] ** 2)[0]  # Ordena pela posição mais próxima
        return None

    def atacar_metin(self, metin_pos):
        """
        Move o mouse até a Metin e clica para atacar.
        """
        if metin_pos:
            pyautogui.moveTo(metin_pos[0], metin_pos[1], duration=0.3)  # Movimento rápido
            time.sleep(2)
            pyautogui.click()  # Clica para atacar
            MetinBotLogger.info(f"Atacando Metin em {metin_pos}")

            # Reduzindo tempo de espera para evitar travamentos
            tempo_maximo = 20  # Tempo máximo esperando ataque (ajustável)
            for _ in range(tempo_maximo // 2):  # Loop de 2s até 20s no máximo
                time.sleep(2)
                MetinBotLogger.info(f"Aguardando destruição ({_ * 2}s)...")

    def pegar_drops(self):
        """
        Pressiona a tecla de coletar os drops.
        """
        time.sleep(1.5)  # Pequeno delay antes da coleta
        pyautogui.press("`")  # Pressiona a tecla de coleta (ao lado do 1)
        MetinBotLogger.info("Coletando drops...")
        time.sleep(1)  # Pequena espera para garantir a coleta

    def iniciar(self):
        """
        Inicia o loop de captura, detecção, ataque e coleta.
        """
        MetinBotLogger.info("Bot em execução...")

        while True:
            frame = self.capturar_tela()
            if frame is None:
                MetinBotLogger.warning("Falha ao capturar tela. Pulando iteração...")
                continue

            results = self.detectar_metins(frame)
            metin_pos = self.encontrar_metin_mais_proxima(results)  # Apenas pega a posição da mais próxima

            if metin_pos:
                MetinBotLogger.info(f"Metin detectada na posição {metin_pos}, atacando...")
                self.atacar_metin(metin_pos)
                self.pegar_drops()

            # Mostrar a detecção ao vivo
            cv2.imshow("Detecção de Metins", frame)

            # Fechar o bot ao pressionar "q"
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.destroyAllWindows()
        MetinBotLogger.info("Bot encerrado.")
