import os
import pygame
from mecanicas_executar import executar_mecanicas
from tutorial import tutorial_game

pygame.mixer.init()

def tocar_musica():
    pygame.mixer.music.load(r"C:\Users\usuario\Documents\GitHub\RPG\Goëtia..mp3") #DEVE-SE ALTERAR PARA O CAMINHO DO SEU REPOSITORIO
    pygame.mixer.music.play(-1)

def tela_bem_vindo():
    print('''
█▀ █▀▀ ░░█ ▄▀█   █▄▄ █▀▀ █▀▄▀█   █░█ █ █▄░█ █▀▄ █▀█   ▄▀█ █▀█   █▀█ █▀█ █▀ █▀ █ █░█ █▀▀ █░░
▄█ ██▄ █▄█ █▀█   █▄█ ██▄ █░▀░█   ▀▄▀ █ █░▀█ █▄▀ █▄█   █▀█ █▄█   █▀▀ █▄█ ▄█ ▄█ █ ▀▄▀ ██▄ █▄▄

█░█ █░░ ▀█▀ █ █▀▄▀█ █▀█   █▀▄ █ ▄▀█   █▀▄ ▄▀█   █▀ █░█ ▄▀█   █░█ █ █▀▄ ▄▀█
█▄█ █▄▄ ░█░ █ █░▀░█ █▄█   █▄▀ █ █▀█   █▄▀ █▀█   ▄█ █▄█ █▀█   ▀▄▀ █ █▄▀ █▀█''')
    print("""
                                                         ,--.             
                                                        {    }            
                                                        K,   }            
                                                        /  `Y`             
                                                   _   /   /               
                                                  {_'-K.__/                
                                                    `/-.__L._              
                                                    /  ' /`\_}             
                                                   /  ' /     
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
    print('1. Iniciar')
    print('2. Tutorial')
    print('3. Sair')

def finalizar_jogo():
    clear_screen()
    print('Jogo encerrado\n')
    input('Aperte qualquer tecla para voltar ao menu inicial...')

def escolher_opcao():
    while True:
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('\nEscolha uma opção: '))
            print(f'Você escolheu a opção {opcao_escolhida}')
            if opcao_escolhida == 1:
                pygame.mixer.music.stop()
                executar_mecanicas()
            elif opcao_escolhida == 2:
                tutorial_game()
                input('Aperte qualquer tecla para voltar ao menu inicial...')
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
            break  # Sai do loop se o jogo foi finalizado

if __name__ == '__main__':
    main()
