import time
import keyboard
from colorama import init, Fore

# Inicializa colorama
init(autoreset=True)

def ataque(timeout, vida_boss):
    print('DEFINIR FUNCIONALIDADE!\n')
    ini_contagem = time.time()
    while True:
        if keyboard.is_pressed('x') or keyboard.is_pressed('b'):
            print('Nossa que ataque brutal, -20 de vida para esse Boss!\n')
            vida_boss -= 20  # Subtrai 20 pontos de vida do boss
            print('Vida do Boss: ')
            mostrar_barra_vida(vida_boss)
            print('\n')
            break
        elif time.time() - ini_contagem >= timeout:
            print("Você não conseguiu atacar, tome cuidado ou ele vai te matar!\n")
            break
        else:
            time_left = int(timeout - (time.time() - ini_contagem))
            print(f'Tempo restante: {time_left} segundos', end='\r')
    return vida_boss

def mostrar_barra_vida(vida):
    tamanho_barra = 20
    vida_atual = max(0, vida)
    percentual_vida = vida_atual / 100.0
    num_simbolos = int(tamanho_barra * percentual_vida)
    barra_vida = f'|{"█" * num_simbolos}{"░" * (tamanho_barra - num_simbolos)}|'
    print(Fore.RED + barra_vida + Fore.RESET)

vida_do_boss = 100  # Definir a vida do monstrin
tempo_limite = 10  # Definir o tempo limite pro ataque

vida_do_boss = ataque(tempo_limite, vida_do_boss)

# Podemos adicionar mais chamadas pra função de 'ataque' para representar mais ataques ou interações do jogador com o boss
