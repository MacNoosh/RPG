import time
import keyboard
from game import *


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
        
def creditos():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA + centralizar_texto('''
Direcao:
Pedro Almeida

Roteiro:
Douglas Vignoli

Edicao e Pos-producao:
Raphael Oliveira

Animacao:
Fabio Souteiro

Consultoria Tecnica:
Neilton Junior '''))
    time.sleep(5)


def game_over():
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
    print(Fore.CYAN + game_over)