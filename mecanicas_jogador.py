import time
import keyboard
from colorama import Fore, Back, Style, init

def print_slow(texto, atraso):
    for x in texto:
        print(x,end="",flush=True)
        time.sleep(atraso)

def atack_1(timeout):
    print('DEFINIR FUNCIONALIDADE!\n')
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('x') or keyboard.is_pressed('b'):
            print('Nosa que ataque brutal, -20 de vida pra esse Boss !\n')
            break
        elif time.time() - ini_contagem >= timeout:
            print("Você não conseguiu atacar, tome cuidado ou ele vai te matar !\n")
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')
        
def atack_2(timeout):
    print_slow("\nDEFINIR FUNCIONALIDADE!\n",atraso=0.02)
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('left') or keyboard.is_pressed('right'):
            print("\nDEFINIR FUNCIONALIDADE!\n")
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nVocê não conseguiu desviar e levou X de dano\n")
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')

def atack_3(timeout):
    print_slow("\nDEFINIR FUNCIONALIDADE!\n",atraso=0.02)
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('up') or keyboard.is_pressed('down'):
            print("\nDEFINIR FUNCIONALIDADE!\n")
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nDEFINIR FUNCIONALIDADE!\n")
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')

def atack_4(timeout):
    print_slow("\nDEFINIR FUNCIONALIDADE!\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('d'):
            print("\nDEFINIR FUNCIONALIDADE!\n") #esse texto vai ser alterado
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nDEFINIR FUNCIONALIDADE!\n") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')
            
def atack_5(timeout):
    print_slow("\nDEFINIR FUNCIONALIDADE!\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('space'):
            print("\nDEFINIR FUNCIONALIDADE!\n") #esse texto vai ser alterado
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nDEFINIR FUNCIONALIDADE!\n") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')  

def atack_6(timeout):
    print_slow("\nADEFINIR FUNCIONALIDADE!\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('down'): #estudar o código que exija 2 teclas em sequencia, não é esse
            print("\nDEFINIR FUNCIONALIDADE!\n")
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nDEFINIR FUNCIONALIDADE!\n") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')

def atack_7(timeout):
    print_slow("\nDEFINIR FUNCIONALIDADE!\n",atraso=0.02) #esse texto vai ser alterado
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('down') and keyboard.is_pressed('left'): #estudar o código que exija 2 teclas em sequencia, não é esse
            print("\nDEFINIR FUNCIONALIDADE!\n")
            break
        elif time.time() - ini_contagem >= timeout:
            print("\nDEFINIR FUNCIONALIDADE!\n") #esse texto vai ser alterado
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')



#teste