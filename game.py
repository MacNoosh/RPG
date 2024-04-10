import os
from random import random
import time
import threading
import keyboard
import mecanicas_boss
import jogador
import tutorial



def tela_bem_vindo():
    print('Seja Bem Vindo ao possivel ultimo dia da sua vida\n\n')

def exibir_opcoes():
    print('1. Iniciar')
    print('2. Tutorial')
    print('3. Sair')

def finalizar_jogo():
    clear_screen()
    print('Jogo encerrado\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')
        if opcao_escolhida == 1:
            mecanicas_boss.mecanica_1(2)
            mecanicas_boss.mecanica_2(2)
            mecanicas_boss.mecanica_3(2)
            mecanicas_boss.mecanica_4(2)
            mecanicas_boss.mecanica_5(2)
            mecanicas_boss.mecanica_6(2)
            jogador.atack_1(2)
        elif opcao_escolhida == 2:
            tutorial.tutorial_game()
        elif opcao_escolhida == 3:
            finalizar_jogo()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def opcao_invalida():
    print("Opção inválida. Por favor, escolha uma das opções disponíveis.")

def main():
    clear_screen()
    tela_bem_vindo()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

