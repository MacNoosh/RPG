import time
import keyboard
from game import *
import os
from colorama import Fore, Style


def esperança(tempo):
    tempo_inicial = time.time()
    resposta = input('.........?: ')
    while True:
        tempo_final = time.time() - tempo_inicial
        if tempo_final >= tempo:
            break
        elif tempo_final < tempo and resposta == 'esperança':
            print('VOCÊ ZEROU O JOGO') #fazer funcao para acabar o game
            break


ultimo_texto = ""
def print_slow(texto, atraso):
    global ultimo_texto
    for x in texto:
        if keyboard.is_pressed('down'):
            clear_screen()
            print(texto)
            break
        else:
            print(x, end="", flush=True)
            ultimo_texto += x
            time.sleep(atraso)

def contador(texto,fim,textofinal):
    contador = 1
    print(texto)
    while fim >= contador:
        print(contador, end = " ", flush = True)
        contador+= 1
        time.sleep(1)
    print(textofinal)


def limpa_linha():
    for _ in range(100):
        keyboard.press_and_release('backspace')
        
def iniciar_jogo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + centralizar_texto("Iniciando novo jogo..."))
    time.sleep(2)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def centralizar_texto(texto, largura=80):
    return texto.center(largura)

def creditos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + centralizar_texto("CREDITOS\n\n\n\n"))
    time.sleep(2)
    print(centralizar_texto("[Cena: Fundo escuro, letras brancas surgem lentamente]\n\n"))
    time.sleep(2)
    print(centralizar_texto("**Créditos Finais**\n\n"))
    time.sleep(1)
    print(centralizar_texto("**Direção Criativa**\n"))
    time.sleep(1)
    print(centralizar_texto("Pedro Almeida\n\n"))
    time.sleep(1)
    print(centralizar_texto("**Roteiro e Produção**\n"))
    time.sleep(1)
    print(centralizar_texto("Douglas Vignoli\n\n"))
    time.sleep(1)
    print(centralizar_texto("**Direção e Pós-produção**\n"))
    time.sleep(1)
    print(centralizar_texto("Raphael Oliveira\n\n"))
    time.sleep(1)
    print(centralizar_texto("**Tester e Produção**\n"))
    time.sleep(1)
    print(centralizar_texto("Fábio Souteiro\n\n"))
    time.sleep(1)
    print(centralizar_texto("**Consultoria Técnica**\n"))
    time.sleep(1)
    print(centralizar_texto("Neilton Júnior\n\n"))
    time.sleep(2)
    print(centralizar_texto("Deu trabalho, mas valeu a pena.\n"))
    time.sleep(3)
    print("[Fecha cortina]")


def game_over():
    os.system('cls' if os.name == 'nt' else 'clear')
    game_over = '''
▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
 ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
 ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                     ░                   
    '''
    game_over = centralizar_texto(game_over)
    print(Fore.RED + game_over)
    
    
    