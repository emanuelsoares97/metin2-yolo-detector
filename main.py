import pyautogui
import time
import cv2
import numpy as np
import mss

# Lista de templates de Metins (adiciona mais imagens se necessário)
metin_templates = ["metin1.png", "metin2.png"]  # Caminhos das imagens de referência

# Coordenadas da tela do jogo (ajustar conforme necessário)
GAME_REGION = {"left": 283, "top": 107, "width": 1590, "height": 888}  # Ajustado para tua resolução

def capturar_tela():
    """ Captura a tela do jogo e aplica um filtro para remover ruídos """
    with mss.mss() as sct:
        screenshot = sct.grab(GAME_REGION)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)  # Converte para cinza
        img = cv2.GaussianBlur(img, (3, 3), 0)  # Suaviza a imagem para remover ruídos
        return img

def carregar_templates():
    """ Carrega templates de Metins do disco """
    templates_carregados = []
    for template_path in metin_templates:
        template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"Erro ao carregar template: {template_path}")
        else:
            templates_carregados.append(template)
            print(f"Template carregado com sucesso: {template_path}")
    return templates_carregados

def encontrar_metin(img_tela, templates):
    """ Procura por Metins na tela testando diferentes escalas do template """
    melhor_correspondencia = 0
    melhor_posicao = None
    melhor_template_tamanho = None

    for template_original in templates:
        # Testar diferentes escalas do template
        for scale in np.linspace(0.7, 1.3, 10):  # Tenta tamanhos de 70% a 130%
            template = cv2.resize(template_original, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
            res = cv2.matchTemplate(img_tela, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

            if max_val > 0.65:  # Threshold ajustado para 0.65 para evitar falsos positivos
                print(f"🔍 Metin detectada ({max_val * 100:.1f}% certeza) em escala {scale:.2f}")

                if max_val > melhor_correspondencia:
                    melhor_correspondencia = max_val
                    melhor_posicao = max_loc
                    melhor_template_tamanho = template.shape  # Guarda o tamanho do template usado

    if melhor_posicao:
        x, y = melhor_posicao
        template_w, template_h = melhor_template_tamanho
        x += template_w // 2
        y += template_h // 2
        print(f"🎯 Coordenadas ajustadas da Metin: ({x}, {y})")
        return x, y
    else:
        print("🚫 Nenhuma Metin encontrada.")
        return None

def visualizar_template(img_tela, posicao):
    """ Desenha um retângulo na tela mostrando onde a Metin foi detectada """
    if posicao:
        x, y = posicao
        cv2.rectangle(img_tela, (x - 25, y - 25), (x + 25, y + 25), (255, 0, 0), 2)
        cv2.imshow("Detecção de Metin", img_tela)
        cv2.waitKey(1000)  # Mostra por 1 segundo
        cv2.destroyAllWindows()

def atacar_metin(posicao):
    """ Move o mouse para a Metin e ataca repetidamente """
    if posicao:
        x, y = posicao
        x += GAME_REGION["left"]  # Ajusta para a posição real na tela
        y += GAME_REGION["top"]

        pyautogui.moveTo(x, y, duration=0.3)
        time.sleep(0.2)
        pyautogui.click()
        print(f"⚔️ Atacando Metin em ({x}, {y})")

        for _ in range(10):  # Ajuste o número de ataques
            pyautogui.press("space")
            time.sleep(0.3)
    else:
        print("❌ Não foi possível atacar nenhuma Metin.")

def mover_personagem():
    """ Move o personagem para encontrar novas Metins """
    movimentos = ["w", "a", "s", "d"]
    direcao = np.random.choice(movimentos)

    print(f"🚶 Movendo-se na direção: {direcao.upper()}")
    pyautogui.keyDown(direcao)
    time.sleep(np.random.uniform(1.5, 3.0))  # Tempo aleatório para parecer mais humano
    pyautogui.keyUp(direcao)

def main():
    """ Loop principal do bot """
    templates = carregar_templates()
    if not templates:
        print("Nenhum template foi carregado com sucesso, encerrando bot.")
        return

    print("🤖 Bot iniciado! Aguardando...")
    time.sleep(2)

    while True:
        tela = capturar_tela()
        posicao_metin = encontrar_metin(tela, templates)
        visualizar_template(tela, posicao_metin)

        if posicao_metin:
            atacar_metin(posicao_metin)
        else:
            print("🔄 Nenhuma Metin visível. Movendo-se para procurar...")
            mover_personagem()

        time.sleep(3)  # Tempo entre cada verificação

if __name__ == "__main__":
    main()
