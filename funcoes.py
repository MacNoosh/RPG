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

def aprendizado(palavra, dano):
    palavras_atk[palavra] = dano
    for key in palavras_dfs_totais:
        if key in palavras_atk:
            palavras_dfs_player[key] = palavras_dfs_totais[key]
