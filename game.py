import os
import random
from tutorial import tutorial_game

def tela_bem_vindo():
    print('Seja Bem Vindo ao possivel ultimo dia da sua vida\n\n')

def exibir_opcoes():
    print('1. Iniciar')
    print('2. Tutorial')
    print('3. Sair')

def finalizar_jogo():
    clear_screen()
    print('Jogo encerrado\n')
    input('Aperte qualquer tecla para voltar ao menu incial...')
    main()
    
def escolher_opcao():
    while True:
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('\nEscolha uma opção: '))
            print(f'Você escolheu a opção {opcao_escolhida}')
            if opcao_escolhida == 1:
                executar_mecanicas()
            elif opcao_escolhida == 2:
                tutorial_game()
            elif opcao_escolhida == 3:
                finalizar_jogo()
                return True  # Retorna o jogo foi finalizado
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()
            
# importação das mecanicas tem que ficar dentro da função pq fora incia o game com uma mecanica random
def executar_mecanicas():
    from mecanicas_boss import mecanica_1, mecanica_2, mecanica_3, mecanica_4, mecanica_5, mecanica_6
    todas_mecanicas = [mecanica_1, mecanica_2, mecanica_3, mecanica_4, mecanica_5, mecanica_6]
    for mecanica in todas_mecanicas:
        mecanica(timeout=random.randint(2, 3))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def opcao_invalida():
    print("Opção inválida. Por favor, escolha uma das opções disponíveis.")

def main():
    jogo_finalizado = False  # adicioneu essa flag pra indicar a finalização do game
    while not jogo_finalizado:
        clear_screen()
        tela_bem_vindo()
        jogo_finalizado = escolher_opcao()

if __name__ == '__main__':
    main()