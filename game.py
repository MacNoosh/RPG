import os
import shutil
import pygame
import time
from colorama import init, Fore, Style
from tutorial import tutorial_game
from historia import *
from funcoes import *

init(autoreset=True)

pygame.mixer.init()

def tocar_musica():
    pygame.mixer.music.load(r"C:\Users\MacNoosh\Documents\GitHub\RPG\Cronus.mp3") #DEVE-SE ALTERAR PARA O CAMINHO DO SEU REPOSITORIO
    pygame.mixer.music.play(-1)

def tocar_musica_2():
    pygame.mixer.music.load(r"C:\Users\MacNoosh\Documents\GitHub\RPG\teste.mp3") #DEVE-SE ALTERAR PARA O CAMINHO DO SEU REPOSITORIO
    pygame.mixer.music.play(-1)

def centralizar_texto(texto):
    largura_terminal = shutil.get_terminal_size().columns
    linhas = texto.split('\n')
    texto_centralizado = ''
    for linha in linhas:
        texto_centralizado += linha.center(largura_terminal) + '\n'
    return texto_centralizado

def tela_bem_vindo():
    nome_jogo = '''
▄████████  ▄█       ████████▄     ▄████████ ███▄▄▄▄           ▄████████     ███        ▄████████  ▄█  ███▄▄▄▄      ▄██████▄  
  ███    ███ ███       ███   ▀███   ███    ███ ███▀▀▀██▄        ███    ███ ▀█████████▄   ███    ███ ███  ███▀▀▀██▄   ███    ███ 
  ███    █▀  ███       ███    ███   ███    █▀  ███   ███        ███    █▀     ▀███▀▀██   ███    ███ ███▌ ███   ███   ███    █▀  
 ▄███▄▄▄     ███       ███    ███  ▄███▄▄▄     ███   ███        ███            ███   ▀  ▄███▄▄▄▄██▀ ███▌ ███   ███  ▄███        
▀▀███▀▀▀     ███       ███    ███ ▀▀███▀▀▀     ███   ███      ▀███████████     ███     ▀▀███▀▀▀▀▀   ███▌ ███   ███ ▀▀███ ████▄  
  ███    █▄  ███       ███    ███   ███    █▄  ███   ███               ███     ███     ▀███████████ ███  ███   ███   ███    ███ 
  ███    ███ ███▌    ▄ ███   ▄███   ███    ███ ███   ███         ▄█    ███     ███       ███    ███ ███  ███   ███   ███    ███ 
  ██████████ █████▄▄██ ████████▀    ██████████  ▀█   █▀        ▄████████▀     ▄████▀     ███    ███ █▀    ▀█   █▀    ████████▀  
             ▀                                                                           ███    ███                              
    '''
    ascii_art = """
⠀⠀⣀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⣠⣤⡀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⢸⣧⠞⠁⡷⢿⣦⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣆⠀⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣼⢪⡇⠀⠀⣷⣶⢹⡇⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠉⠉⠉⢩⠉⠙⠛⣿⠛
⣿⣿⣿⣿⣿⣿⣷⡄⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢹⠘⣷⣄⢳⣿⣿⣾⣗⡿⠀⠀⠀⠀⢀⣟⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀
⣿⣿⣿⣿⣿⣿⡍⠉⠀⠘⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠿⡄⠀⠀⠀⢸⠆⣿⣿⡏⣿⣿⣿⡗⣧⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣄⢧⡀⣀⡴⠋⢀⣿⣿⣷⣿⣿⣿⡇⢩⡳⢤⣀⢠⣿⣟⣿⣿⠀⢀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⢫⠿⠟⢳⡇⠀⣼⣿⣿⣿⣿⣿⣿⣷⡀⢸⣷⡿⠟⠛⠛⢿⣿⣦⠓⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠑⠉⠀⠀⣾⡴⣾⡿⢹⠙⢿⡭⠭⠽⢿⣿⣿⡿⣅⣀⣀⣀⣰⣿⡟⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⢹⠋⠙⠛⢻⡿⣡⣿⠃⣸⡇⠈⠓⢤⣀⠈⠁⣿⡤⢤⣤⣬⠟⢻⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⡼⢀⣠⣴⣿⡟⠛⠁⠀⡏⠀⠀⠀⠂⢹⣷⣤⣾⣧⣶⣾⡍⢛⣿⣿⣿⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⣼⡵⠋⢹⣿⣿⣧⠀⠀⠀⡷⠀⠸⡷⣤⣴⡿⣿⣿⣿⣿⣵⣿⣶⣿⣿⡛⠒⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠂⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠃⠀⠀⠀⠀⠀⠀⡼⠛⢻⣿⡀⠀⠀⣇⣀⡆⣀⣼⣟⡂⣹⣿⣿⠻⣧⠀⠈⠉⣻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⠀⢀⡌⠀⠀⠀⠀
⡟⠛⠛⠛⠛⠛⠛⠛⠛⠛⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⢀⣼⣧⣤⣼⣿⡇⠀⠀⣿⢿⣼⠟⠋⠹⣿⣿⣿⡏⠀⠹⣦⣤⣾⡿⣻⣟⣛⣦⡄⠀⠀⠀⠀⢠⠞⠁⠀⢠⠞⠀⠀⠀⠀⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⢹⣿⣿⣿⣿⡟⠳⡄⣿⣾⣿⠾⠿⠿⣿⡿⢿⠁⠀⠀⠹⣿⡿⠾⣿⣿⡅⢸⠃⠀⠀⢀⡴⠋⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠙⣿⣿⣿⡇⢄⠈⢿⡿⢁⣴⡾⢿⢿⣿⣿⣇⠀⠀⠘⣿⡁⠠⣿⣿⠳⡾⠀⢀⡴⠋⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⢀⣼⠟⣿⣟⡀⠈⠑⣿⣿⣿⣭⣷⢾⣿⣿⣿⠿⣦⠀⠀⠹⣷⠈⢹⣿⣦⣵⡴⠋⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠡⠀⣴⢿⡾⠛⠀⣹⣆⠀⣸⣿⣿⣭⣾⡟⠻⣥⣐⣦⠈⡇⠀⠀⢹⡄⢸⣿⡇⡏⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⢟⣿⣿⠟⢠⢃⡼⣿⡟⢷⣸⣿⣿⣿⣿⣿⣦⡈⠻⠛⠉⢳⠀⢐⣿⣧⠈⣿⡋⠁⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⢛⣾⣿⠋⢀⡼⠋⠀⣿⡇⠈⢻⢟⡟⣿⣿⣿⠙⣿⣦⣶⡖⠒⣷⣾⣿⡟⢳⣿⡗⢶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⣼⣿⣧⣤⡾⠁⠀⣀⣿⡇⠇⢀⡾⡇⣿⣧⣿⠀⠸⣿⣿⣿⠲⣼⠻⢿⣇⣺⣿⣧⣼⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⠃⢠⡾⠁⢹⡇⠀⠚⠁⣷⣿⠷⠘⢷⡄⠀⠀⢹⡆⢸⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⣀⣤⣿⣿⣿⡿⢸⣿⠁⠀⢸⣷⠀⠀⢸⢹⣿⣗⠂⠀⠹⣆⠀⠈⣿⢸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢬⣹⣿⢿⣿⣿⡿⠋⠀⣾⡇⣠⣴⣿⣿⢦⡀⣼⣸⣿⣿⣦⡀⠀⢹⡆⠂⣿⣿⣿⣿⣿⣿⠛⢦⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠟⣻⢿⣿⣯⣀⡀⣼⣿⠋⠁⣈⣿⣿⣷⣻⣿⣿⣿⣿⣿⣁⣀⢸⣿⣶⣿⣿⣿⣿⣿⣿⣷⡈⢧⡘⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣯⠞⠁⣠⠿⠛⠻⢱⣿⡇⠠⠾⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⡻⣿⣿⣿⣆⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢞⣿⠏⠀⣰⠋⠀⠀⠀⢀⣿⡟⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣬⣭⣿⣿⣿⣦⣝⢷⣄⠙⢿⣿⣷⣌⠃⢀⠀⠀⠀⠏⠉⠛⠳⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⡴⢫⠞⠁⢀⡾⠁⠀⠀⠀⠀⣼⣿⣠⡶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡟⢿⣿⣿⣯⡳⣝⠷⣿⣿⣟⠿⠻⢦⣄⡀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⠋⡴⠃⢀⡴⠋⠀⠀⠀⠀⣠⢰⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⢸⣿⣿⣿⣿⣾⣿⣿⠿⡟⠶⣤⣄⡙⠙⢦⣝⠷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡴⠃⠈⢀⣴⠋⠀⠀⠀⠀⠀⢠⢧⣿⣿⣿⢣⡿⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣍⠙⠳⢶⣌⠁⠈⢳⡄⠀⠀⠀⠀
⠀⠀⠀⠀⣸⠁⣀⡴⠛⠁⠀⠀⠀⠀⠀⢠⢏⣿⣿⣿⠹⡟⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣙⠓⠈⠀⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠻⠚⠁⠀⠀⠀⠀⠀⠀⠀⢠⣟⣾⣿⣿⣿⠀⡴⠋⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣃⡃⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⠴⠒⢋⣾⣿⣿⣿⠇⡀⠂⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣙⡇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠠⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣶⣎⣁⣀⣀⣼⣿⣿⣿⣿⡮⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⢻⡇⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    nome_jogo = centralizar_texto(nome_jogo)
    ascii_art = centralizar_texto(ascii_art)

    print(Fore.CYAN + nome_jogo)
    print(Fore.RED + ascii_art)
    print(Fore.CYAN + centralizar_texto("Pressione ENTER para iniciar"))

def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    tocar_musica()
    tela_bem_vindo()
    input()
    jogar()

def jogar():
    opcao = ""
    while opcao != "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(centralizar_texto("1. Novo Jogo"))
        print(centralizar_texto("2. Tutorial"))
        print(centralizar_texto("3. Créditos"))
        print(centralizar_texto("0. Sair"))
        opcao = input(Fore.CYAN + centralizar_texto("Escolha uma opção: "))

        if opcao == "1":
            iniciar_jogo()
            tocar_musica_2()
            historia()
            game_over()
        elif opcao == "2":
            tutorial_game()
        elif opcao == "3":
            creditos()
        elif opcao == "0":
            print(Fore.CYAN + centralizar_texto("Saindo do jogo..."))
            time.sleep(2)
        else:
            print(Fore.RED + centralizar_texto("Opção inválida! Tente novamente."))
            time.sleep(2)

def iniciar_jogo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + centralizar_texto("Iniciando novo jogo..."))
    time.sleep(2)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    

if __name__ == "__main__":
    menu_principal()
