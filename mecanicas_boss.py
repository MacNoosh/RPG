from colorama import Fore, Back, Style, init
import time
import keyboard

def print_slow(texto, atraso):
    for x in texto:
        print(x,end="",flush=True)
        time.sleep(atraso)
        

def mecanica_1(timeout):
    print_slow("\nO BOSS ESTÁ PREPARANDO UM GOLPE FRONTAL. RÁPIDO !! DESVIE PARA O LADO!!!\n",atraso=0.02)
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('left') or keyboard.is_pressed('right'):
            print("\nVocê desviou do ataque!\n")
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nVocê não conseguiu desviar e levou X de dano\n")
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')

def mecanica_2(timeout):
    print_slow("\nO BOSS ESTÁ PREPARANDO UM NOVO ATAQUE, DESSA VEZ ELE ESTÁ COM RAIVA!\n",atraso=0.02)
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('up') or keyboard.is_pressed('down'):
            print("\nVocê foi mais rápido e desviou do ataque!\n")
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nVocê não conseguiu desviar e levou X de dano\n")
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')

def mecanica_3(timeout):
    print_slow("\nATAQUE DE ARMA DO BOSS, USE O ESCUDO!\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('d'):
            print("\nVocê bloqueou o ataque!\n") #esse texto vai ser alterado
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nVocê não conseguiu bloquear e recebeu X dano\n") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')
            
def mecanica_4(timeout):
    print_slow("\nGOLPE RASTEIRO, PULE!\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('space'):
            print("\nVocê saltou o ataque!\n") #esse texto vai ser alterado
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nVocê não conseguiu pular e recebeu X dano\n") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')  

def mecanica_5(timeout):
    print_slow("\nAPROXIMAÇÃO DO BOSS, RECUE!!\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('down'): #estudar o código que exija 2 teclas em sequencia, não é esse
            print("\nVocê saltou o ataque!\n")
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nVocê não conseguiu pular e recebeu X dano\n") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')

def mecanica_6(timeout):
    print_slow("\nALGUM ATAQUE DO BOSS!! ROLE PARA O LADO\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('down') and keyboard.is_pressed('left'): #estudar o código que exija 2 teclas em sequencia, não é esse
            print("\nVocê rolou o ataque!\n")
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nVocê não conseguiu rolar e recebeu X dano\n") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')
                

