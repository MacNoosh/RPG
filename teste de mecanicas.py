import os
import random
import time
import tutorial
import keyboard

def tela_bem_vindo():
    print('Seja Bem Vindo ao possivel ultimo dia da sua vida\n\n')

def exibir_opcoes():
    print('1. Iniciar')
    print('2. Tutorial')
    print('3. Sair')

def finalizar_jogo():
    clear_screen()
    print('Jogo encerrado\n')
    input('Pressione Enter para voltar ao menu inicial...')

def escolher_opcao():
    while True:
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('\nEscolha uma opção: '))
            print(f'Você escolheu a opção {opcao_escolhida}')
            if opcao_escolhida == 1:
                executar_mecanicas()
            elif opcao_escolhida == 2:
                tutorial.tutorial_game()
            elif opcao_escolhida == 3:
                finalizar_jogo()
                return True
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()

def executar_mecanicas():
    mecanicas = [mecanica_1]
    for mecanica in mecanicas:
        if not mecanica():
            print("Você não conseguiu desviar e levou dano!")
            return False
    else:
        print("Você desviou de todos os ataques!")
        return True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def opcao_invalida():
    print("Opção inválida. Por favor, escolha uma das opções disponíveis.")

def mecanica_1():
    print("O Boss está vindo em sua direção, rápido RECUE!")
    start_time = time.time()
    sequence = ["down", "down"]
    input_sequence = []
    while True:
        if keyboard.is_pressed("down"):
            input_sequence.append("down")
            time.sleep(0.2)  # Aguarda um pequeno intervalo para evitar múltiplas detecções de tecla
        elif keyboard.is_pressed("down"):
            input_sequence.append("down")
            time.sleep(0.2)
        if input_sequence == sequence:
            return True
        elif time.time() - start_time >= 3:  # Tempo limite de 3 segundos
            return False

#def mecanica_2():
    # Implemente sua segunda mecânica aqui
    #print("Implemente sua segunda mecânica aqui")
    #return True  # Simula que o jogador desviou com sucesso

# Implemente as outras mecânicas de forma semelhante

def main():
    while True:
        clear_screen()
        tela_bem_vindo()
        if escolher_opcao():
            break

if __name__ == '__main__':
    main()
