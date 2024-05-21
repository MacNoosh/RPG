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
        elif tempo_final < tempo or resposta == 'esperança':
            print('VOCÊ ZEROU O JOGO') #fazer funcao para acabar o game
            break

esperança(2.5)

print_slow('alow alow alow alow', 0.048)