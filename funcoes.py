import time
import keyboard


def esperança(tempo):
    tempo_inicial = time.time()
    resposta = input('.........?: ')
    while True:
        tempo_final = time.time() - tempo_inicial
        if tempo_final >= tempo:
            break
        elif tempo_final < tempo or resposta == 'esperança':
            print('VOCÊ ZEROU O JOGO')
            break