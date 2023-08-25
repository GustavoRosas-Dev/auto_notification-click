# Autor: Gustavo Rosas
# GitHub: https://github.com/GustavoRosas-Dev/auto_notification-click
# Data: 2023-08-25

import pyautogui  # Importa a biblioteca para automação de GUI
import keyboard  # Importa a biblioteca para interação com o teclado
import time  # Importa a biblioteca para gerenciamento de tempo
import PySimpleGUI as sg  # Importa a biblioteca para criação de GUI

# Define o tema
sg.theme("LightGrey1") # Outras opções: [‘Black’, ‘BlueMono’, ‘BluePurple’, ‘BrightColors’, ‘BrownBlue’, ‘Dark’, ‘Dark2’, ‘DarkAmber’, ‘DarkBlack’, ‘DarkBlack1’, ‘DarkBlue’, ‘DarkBlue1’, ‘DarkBlue10’, ‘DarkBlue11’, ‘DarkBlue12’, ‘DarkBlue13’, ‘DarkBlue14’, ‘DarkBlue15’, ‘DarkBlue16’, ‘DarkBlue17’, ‘DarkBlue2’, ‘DarkBlue3’, ‘DarkBlue4’, ‘DarkBlue5’, ‘DarkBlue6’, ‘DarkBlue7’, ‘DarkBlue8’, ‘DarkBlue9’, ‘DarkBrown’, ‘DarkBrown1’, ‘DarkBrown2’, ‘DarkBrown3’, ‘DarkBrown4’, ‘DarkBrown5’, ‘DarkBrown6’, ‘DarkGreen’, ‘DarkGreen1’, ‘DarkGreen2’, ‘DarkGreen3’, ‘DarkGreen4’, ‘DarkGreen5’, ‘DarkGreen6’, ‘DarkGrey’, ‘DarkGrey1’, ‘DarkGrey2’, ‘DarkGrey3’, ‘DarkGrey4’, ‘DarkGrey5’, ‘DarkGrey6’, ‘DarkGrey7’, ‘DarkPurple’, ‘DarkPurple1’, ‘DarkPurple2’, ‘DarkPurple3’, ‘DarkPurple4’, ‘DarkPurple5’, ‘DarkPurple6’, ‘DarkRed’, ‘DarkRed1’, ‘DarkRed2’, ‘DarkTanBlue’, ‘DarkTeal’, ‘DarkTeal1’, ‘DarkTeal10’, ‘DarkTeal11’, ‘DarkTeal12’, ‘DarkTeal2’, ‘DarkTeal3’, ‘DarkTeal4’, ‘DarkTeal5’, ‘DarkTeal6’, ‘DarkTeal7’, ‘DarkTeal8’, ‘DarkTeal9’, ‘Default’, ‘Default1’, ‘DefaultNoMoreNagging’, ‘Green’, ‘GreenMono’, ‘GreenTan’, ‘HotDogStand’, ‘Kayak’, ‘LightBlue’, ‘LightBlue1’, ‘LightBlue2’, ‘LightBlue3’, ‘LightBlue4’, ‘LightBlue5’, ‘LightBlue6’, ‘LightBlue7’, ‘LightBrown’, ‘LightBrown1’, ‘LightBrown10’, ‘LightBrown11’, ‘LightBrown12’, ‘LightBrown13’, ‘LightBrown2’, ‘LightBrown3’, ‘LightBrown4’, ‘LightBrown5’, ‘LightBrown6’, ‘LightBrown7’, ‘LightBrown8’, ‘LightBrown9’, ‘LightGray1’, ‘LightGreen’, ‘LightGreen1’, ‘LightGreen10’, ‘LightGreen2’, ‘LightGreen3’, ‘LightGreen4’, ‘LightGreen5’, ‘LightGreen6’, ‘LightGreen7’, ‘LightGreen8’, ‘LightGreen9’, ‘LightGrey’, ‘LightGrey1’, ‘LightGrey2’, ‘LightGrey3’, ‘LightGrey4’, ‘LightGrey5’, ‘LightGrey6’, ‘LightPurple’, ‘LightTeal’, ‘LightYellow’, ‘Material1’, ‘Material2’, ‘NeutralBlue’, ‘Purple’, ‘Reddit’, ‘Reds’, ‘SandyBeach’, ‘SystemDefault’, ‘SystemDefault1’, ‘SystemDefaultForReal’, ‘Tan’, ‘TanBlue’, ‘TealMono’, ‘Topanga’]

# Variáveis
conf = 0.8  # Configuração de confiança para localização de imagens
aguardar = 0.2  # Tempo de espera padrão

# Identidade Visual
cor_destaque = "#008afc"
cor_botao = "#fff"
cor_descricao = "#1d2226"

# Fonte
font = 'Helvetica'

# Ícone
icon = 'images/ico/icon.ico'

def localizar_e_fechar_popup_e_clicar(popup_img, click_img):
    while True:
        # Localiza a posição da imagem do popup na tela
        popup_cords = pyautogui.locateOnScreen(image=popup_img, confidence=conf)

        # Localiza a posição da imagem do local do clique na tela
        click_cords = pyautogui.locateOnScreen(image=click_img, confidence=conf)

        if popup_cords and click_cords:
            print("Achei o popup e o local do clique.")
            time.sleep(aguardar)

            # Trecho opcional para clicar no popup e fechá-lo
            # pyautogui.click(popup_cords)
            # print("Cliquei para fechar o popup.")
            # time.sleep(aguardar)

            # Clica na posição identificada como local de clique
            pyautogui.click(click_cords)
            print("Cliquei no local desejado.")
        else:
            print("Procurando...")
            time.sleep(aguardar + 0.3)

        # Verifica se a tecla 'CTRL+C' foi pressionada para interromper o programa
        if keyboard.is_pressed('ctrl+c'):
            print("Programa interrompido pelo usuário")
            break


def main():
    # Define o layout da interface gráfica
    layout = [
    [sg.Text("Selecione a imagem do 'popup':", font=(font, 10, "bold"), text_color=cor_destaque)],
    [sg.InputText(key="popup_imagem", size=(50, 1), font=(font, 9)), sg.FileBrowse(button_text='procurar', font=(font, 8), button_color=cor_destaque)],
    [sg.Text("Selecione a imagem do 'local do clique':", font=(font, 10, "bold"), text_color=cor_destaque)],
    [sg.InputText(key="clique_imagem", size=(50, 1), font=(font, 9)), sg.FileBrowse(button_text='procurar', font=(font, 8), button_color=cor_destaque)],
    [sg.Button("Iniciar", font=(font, 10, "bold"), button_color=cor_destaque), sg.Text("Obs: Pressione 'CTRL+C' para pausar a qualquer momento.", font=(font, 8), text_color=cor_descricao)]
]

    # Cria a janela de GUI com o layout especificado
    window = sg.Window("Auto Notification-Click", layout, icon=icon)

    while True:
        # Aguarda por eventos da janela
        event, values = window.read()

        # Verifica se a janela foi fechada
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Iniciar":
            popup_img_path = values["popup_imagem"]
            clique_img_path = values["clique_imagem"]
            localizar_e_fechar_popup_e_clicar(popup_img_path, clique_img_path)

    # Fecha a janela ao finalizar o programa
    window.close()


# Chama a função main quando o script é executado diretamente (e naõ como um módulo/import)
if __name__ == "__main__":
    main()
