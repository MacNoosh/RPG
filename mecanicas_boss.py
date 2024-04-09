import time
import keyboard
from colorama import Fore, Back, Style, init

def print_slow(texto, atraso):
    for x in texto:
        print(x,end="",flush=True)
        time.sleep(atraso)
        
def mecanica_1(timeout):
    print_slow("O Boss está preparando um golpe frontal. Rápido!! Desvie para o lado!!!\n",atraso=0.02)
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('left') or keyboard.is_pressed('right'):
            print("Você desviou do ataque! \n")
            break
        elif time.time() - ini_contagem >= timeout:
            print("Você não conseguiu desviar e levou X de dano\n")
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')

def mecanica_2(timeout):
    print_slow("O boss está preparando um novo ataque, dessa vez ele está com raiva !\n",atraso=0.02)
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('up') or keyboard.is_pressed('down'):
            print("Você foi mais rápido e desviou do ataque!\n")
            break
        elif time.time() - ini_contagem >= timeout:
            print("Você não conseguiu desviar e levou X de dano\n")
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')

