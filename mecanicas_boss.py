import time
import keyboard
from colorama import Fore, Back, Style, init
import random

def print_slow(texto, atraso):
    for x in texto:
        print(x,end="",flush=True)
        time.sleep(atraso)
        
        
def mecanica_1(timeout):
    print_slow("O Boss está preparando um golpe frontal. Rápido!! Desvie para o lado!!!\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('left') or keyboard.is_pressed('right'): #esse texto vai ser alterado
            print("Você desviou do ataque!")
            break
        elif time.time() - ini_contagem >= timeout:
            print("Você não conseguiu desviar e levou X de dano") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')

def mecanica_2(timeout):
    print_slow("O boss está preparando um novo ataque, dessa vez ele está com raiva !\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('up') or keyboard.is_pressed('down'):
            print("Você foi mais rápido e desviou do ataque!") #esse texto vai ser alterado
            break
        elif time.time() - ini_contagem >= timeout:
            print("Você não conseguiu desviar e levou X de dano") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')

def mecanica_3(timeout):
    print_slow("ATAQUE DE ARMA DO BOSS, USE O ESCUDO!",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('d'):
            print("Você bloqueou o ataque!") #esse texto vai ser alterado
            break
        elif time.time() - ini_contagem >= timeout:
            print("Você não conseguiu bloquear e recebeu X dano") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')
            
def mecanica_4(timeout):
    print_slow("GOLPE RASTEIRO, PULE!\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('space'):
            print("Você saltou o ataque!") #esse texto vai ser alterado
            break
        elif time.time() - ini_contagem >= timeout:
            print("Você não conseguiu pular e recebeu X dano\n") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')  

def mecanica_5(timeout):
    print_slow("APROXIMAÇÃO DO BOSS, RECUE!!\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('down'): #estudar o código que exija 2 teclas em sequencia, não é esse
            print("Você saltou o ataque!")
            break
        elif time.time() - ini_contagem >= timeout:
            print("Você não conseguiu pular e recebeu X dano\n") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')

def mecanica_6(timeout):
    print_slow("ALGUM ATAQUE DO BOSS!! ROLE PARA O LADO\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('down') and keyboard.is_pressed('left'): #estudar o código que exija 2 teclas em sequencia, não é esse
            print("Você rolou o ataque!")
            break
        elif time.time() - ini_contagem >= timeout:
            print("Você não conseguiu rolar e recebeu X dano\n") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')      
                
todas_mecanicas = [mecanica_1, mecanica_2, mecanica_3,mecanica_4,mecanica_5,mecanica_6]
sortear_mecanica = random.choice(todas_mecanicas)
sortear_mecanica(random.randint(2,3))
