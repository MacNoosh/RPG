import os
import pygame
import time
import keyboard
from colorama import init, Fore, Style
from mecanicas_executar import executar_mecanicas
from tutorial import tutorial_game
from historia import *
from funcoes import *

init(autoreset=True)

pygame.mixer.init()

            
def tocar_musica():
    pygame.mixer.music.load(r"C:\Users\pedro\Documents\GitHub\RPG-python-main\Cronus.mp3") #DEVE-SE ALTERAR PARA O CAMINHO DO SEU REPOSITORIO
    pygame.mixer.music.play(-1)

def tocar_musica_2():
    pygame.mixer.music.load(r"C:\Users\pedro\Documents\GitHub\RPG-python-main\teste.mp3") #DEVE-SE ALTERAR PARA O CAMINHO DO SEU REPOSITORIO
    pygame.mixer.music.play(-1)

def tela_bem_vindo():
            print_slow(f'''
█▀ █▀▀ ░░█ ▄▀█   █▄▄ █▀▀ █▀▄▀█   █░█ █ █▄░█ █▀▄ █▀█   ▄▀█ █▀█   █▀█ █▀█ █▀ █▀ █ █░█ █▀▀ █░░
▄█ ██▄ █▄█ █▀█   █▄█ ██▄ █░▀░█   ▀▄▀ █ █░▀█ █▄▀ █▄█   █▀█ █▄█   █▀▀ █▄█ ▄█ ▄█ █ ▀▄▀ ██▄ █▄▄

█░█ █░░ ▀█▀ █ █▀▄▀█ █▀█  █▀▄ █ ▄▀█   █▀▄ ▄▀█   █▀ █░█ ▄▀█   █░█ █ █▀▄ ▄▀█
█▄█ █▄▄ ░█░ █ █░▀░█ █▄█  █▄▀ █ █▀█   █▄▀ █▀█   ▄█ █▄█ █▀█   ▀▄▀ █ █▄▀ █▀█

''',atraso=0.01)
            ini_contagem = time.time()
            
            
            print("""
                                                         ,--.             
                                                        {    }            
                                                        K,   }            
                                                       /  `Y`             
                                                  _   /   /               
                                                 {_'-K.__/                
                                                   `/-.__L._              
                                                   /  ' /`\_}                 
                                           ____   /  ' /                   
                                    ,-'~~~~    ~~/  ' /_                   
                                  ,'             ``~~~%%',                 
                                (                     %  Y                
                                {     ELDEN {str}ING   %% I                
                               {      -                 %  `.              
                              |       ',                %  )              
                              |        |   ,..__      __. Y               
                              |    .,_./  Y ' / ^Y   J   )|               
                              \           |' /   |   |   ||               
                               \          L_/    . _ (_,.'(               
                                \,   ,      ^^""' / |      )              
                                 \_  \          /,L]     /               
                                   '-_`-,       ` `   ./`                
                                      `-(_            )                  
                                         ^^\..___,.--`                  
                    """)
     
def exibir_opcoes():
    print(f"1. {Fore.RED}Iniciar{Style.RESET_ALL}")
    print(f"2. {Fore.RED}Tutorial{Style.RESET_ALL}")
    print(f"3. {Fore.RED}Sair{Style.RESET_ALL}")
    
def finalizar_jogo():
    clear_screen()
    print('Jogo encerrado\n')
    input('Aperte qualquer tecla para voltar ao menu inicial...')

def escolher_opcao():
    while True:
        exibir_opcoes()
        try:
            opcao_escolhida = int(input(f'\n{Fore.RED}Escolha uma opção:{Style.RESET_ALL}  '))
            print(f'Você escolheu a opção {opcao_escolhida}')
            if opcao_escolhida == 1:
                pygame.mixer.music.stop()
                clear_screen()
                tocar_musica_2()
                historia()
                executar_mecanicas()
                finalizar_jogo()
                main()
            elif opcao_escolhida == 2:
                tutorial_game()
                input('Aperte qualquer tecla para voltar ao menu inicial...')
                main()
            elif opcao_escolhida == 3:
                finalizar_jogo()
                return True  # Retorna True para indicar que o jogo foi finalizado
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()
            
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def opcao_invalida():
    print("Opção inválida. Por favor, escolha uma das opções disponíveis.")

def main():
    while True:
        clear_screen()
        tela_bem_vindo()
        tocar_musica()  # Inicie a reprodução da música
        if escolher_opcao():
            break  # Sai do loop se o jogo foi finalizado0

if __name__ == '__main__':
    main()




