import os
import time
import threading
import keyboard
import mecanicas_boss
import jogador
import tutorial
from pygame import mixer

#teste222

MUSIC_FILE = 'mcpoze.mp3'

def tela_bem_vindo():
    print('Seja Bem Vindo ao possivel ultimo dia da sua vida\n\n')

def play_music():
    mixer.init()
    mixer.music.load(MUSIC_FILE)
    mixer.music.play()

def exibir_opcoes():
    print('1. Iniciar')
    print('2. Iniciar Jogo Salvo')
    print('3. Tutorial')
    print('4. Sair')

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
            jogador.atack_1(2)
        elif opcao_escolhida == 2:
            iniciar_jogo_salvo()  # Not implemented 
        elif opcao_escolhida == 3:
            tutorial.tutorial_game()
        elif opcao_escolhida == 4:
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
    music_thread = threading.Thread(target=play_music)
    music_thread.start()
    main()

