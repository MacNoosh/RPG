import time
import keyboard
from colorama import Fore, Back, Style, init
from funcoes import *
import random

def tutorial_atk(tempo):
    tempo_inicial = time.time()
    palavra = input('Diga a palavra de ATAQUE que você aprendeu até agora: ')
    while True:
        tempo_final = time.time() - tempo_inicial
        if tempo_final >= tempo:
            print(f'Demorou muito ({tempo_final:.1f} segundos)! Diga mais rápido!')
            tutorial_atk(tempo)
            break
        elif tempo_final < tempo and palavra == 'corte':
            print(f'Legal! Você executou o seu ataque em {tempo_final:.1f} segundos. Lembre-se, quanto mais veloz, mais eficaz será o seu golpe!') 
            break
        else:
            print('Você não usou a palavra correta. Tente novamente.')
            tutorial_atk(tempo)
            break

def tutorial_defesa(tempo):
    tempo_inicial = time.time()
    palavra = input('Agora vamos treinar sua defesa, diga a palavra de DEFESA que você aprendeu até agora: ')
    while True:
        tempo_final = time.time() - tempo_inicial
        if tempo_final >= tempo:
            print(f'Demorou muito ({tempo_final:.1f} segundos)! Diga mais rápido!')
            tutorial_defesa(tempo)
            break
        elif tempo_final < tempo and palavra == 'finta':
            print(f'Legal! Você executou o seu ataque em {tempo_final:.1f} segundos. A defesa também se aproveitará da sua agilidade!') 
            break
        else:
            print('Você não usou a palavra correta. Tente novamente.')
            tutorial_defesa(tempo)
            break

def tutorial_desvio(tempo):
    tempo_inicial = time.time()
    print('DESVIE PARA A ESQUERDA')
    while True:
        tempo_final = time.time() - tempo_inicial
        if tempo_final > tempo:
            print('DEMOROU MUITO! Foi golpeado, tente novamente')
            tutorial_desvio(tempo)
            break
        
        elif keyboard.is_pressed('left'):
            print(f'Belo desvio! Desviou em {tempo_final:.1f}s')
            contador('Prepare-se',3,'')
            print('AGORA DESVIE PARA A DIREITA!')
            tempo_inicial = time.time()
            while True:
                tempo_final = time.time() - tempo_inicial
                if tempo_final > tempo:
                    print('DEMOROU MUITO! Foi golpeado, tente novamente')
                    tutorial_desvio(tempo)
                    break
                elif keyboard.is_pressed('right'):
                    print(f'Belo desvio! Desviou em {tempo_final:.1f}s')
                    print('Você concluiu o tutorial!')
                    break
            break

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

def desvio_animado(texto,tecla,tempo,emoji):
    lista = 0
    while lista == 0:
        for i in range(1, 130, 1):
            print(emoji.rjust(i))
            time.sleep(0.05)
            clear_screen()
            if i == random.randint(60,109):
                print(texto.rjust(i))

                desviou = False
                for x in range(tempo*10):
                    if keyboard.is_pressed(tecla):
                        lista += 1
                        print('Você desviou!')
                        desviou = True
                        break
                    time.sleep(0.1)
                if not desviou:
                    print('Você perdeu!')
                    lista += 1
                    break

                break


