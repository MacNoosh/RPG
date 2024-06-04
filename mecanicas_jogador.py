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

# ultimas atualizações, é a que mais gostei até agora:
def atacar(tempo_acao, inimigo, dano):
    global vida_inimigo
    global vida_player
    frases = ['Você vê uma abertura. É sua vez de atacar! ',f'O {inimigo} está vulnerável! Aproveite sua chance! ', 'Você sente a adrenalina. Qual é sua ação? ', 'Agora é com você! Prepare-se para atacar: ']
    errou = [f'Infelizmente, seu ataque não encontra o {inimigo}.', f'Seu ataque falha, deixando o {inimigo} ileso.', f'Apesar de seus esforços, você não consegue acertar o {inimigo}.', f'Seu golpe passa raspando, mas não acerta o {inimigo}.']
    demorou = [f'Você hesita por um momento e perde sua oportunidade de agir. O que permitiu que o {inimigo} lhe golpeasse, causando ', f'Sua hesitação permite ao {inimigo} agir antes de você, e lhe causar', f'Sua indecisão custa caro, e o {inimigo} aproveita a chance, causando ']
    tempo_inicial = time.time()
    print_slow(random.choice(frases),0.02)
    acao = input('')
    
    while True:
        tempo_final = time.time() - tempo_inicial

        if tempo_acao <= tempo_final:
            print_slow(random.choice(demorou), f'{dano} de dano',0.02)
            vida_player -= dano
            break
        
        else:
            if acao in palavras_atk:
                acerto = round(palavras_atk[acao] * 2 * (tempo_acao - tempo_final))
                acertou = [f'Você desfere um {acao.upper()} certeiro!', f'Você desfere um {acao.upper()} devastador no {inimigo}!', f'Seu {acao.upper()} encontra {inimigo} com precisão!']
                print_slow(f'{random.choice(acertou)} causando {acerto} de dano',0.02)
                vida_inimigo-=acerto
                break
            elif acao not in palavras_atk:
                print_slow(random.choice(errou),0.02)
                break
            
def defender_2(tempo_acao, inimigo, dano):
    global vida_inimigo
    global vida_player
    tempo_inicial = time.time()    
    
    defesa_exigida = random.choice(list(palavras_dfs_player.values()))
    palavra_digitada = ''
    
    frases = [f'Seus instintos alertam você sobre o ataque iminente do {inimigo}. Rápido! Use: {defesa_exigida.upper()}', 
              f'O {inimigo} faz um movimento agressivo em sua direção. Será necessário {defesa_exigida.upper()}',
              f'O {inimigo} lança um olhar de desafio em sua direção, pronto para testar sua {defesa_exigida.upper()}.',
              f'O som de passos pesados ecoa ao seu redor, anunciando a investida iminente do {inimigo}. É hora de mostrar sua {defesa_exigida.upper()}!']
    print_slow(random.choice(frases),0.02)
    
    defendeu = [f'Você antecipa os movimentos do {inimigo} com uma precisão impressionante, bloqueando seu ataque com um {defesa_exigida} rápido e eficaz!',
                f'Você se move com uma graça surpreendente, desviando habilmente do ataque do {inimigo}. Sua {defesa_exigida} é impecável!']
    contra = f'Com um movimento fluído, você desvia o ataque do {inimigo}, transformando seu ímpeto ofensivo em uma oportunidade de contra-ataque. Sua defesa não só protege, mas também surpreende!'
    
    sofreu = [f'O golpe do {inimigo} encontra seu caminho através de suas defesas, deixando uma sensação de impacto brutal em seu corpo.',
              f'Você é pego desprevenido pelo ataque do {inimigo}, que encontra sua brecha.',
              f'Você se vê cercado pela dor do ataque do {inimigo}, que parece encontrar uma fraqueza em suas defesas e explorá-la ao máximo.']
    
    while True:
        tempo_final = time.time() - tempo_inicial
        
        if tempo_final > tempo_acao:
            print_slow(f'{random.choice(sofreu)} Você recebeu {dano} de dano.',0.02)
            vida_player-=dano
            break

        tecla = keyboard.read_event()
        if tecla.event_type == keyboard.KEY_DOWN and tecla.name in 'abcdefghijlmnopqrstuvxzkwyãê~^-':
            digitacao = tecla.name
            palavra_digitada += digitacao
            print(digitacao, end = '', flush=True)

        if palavra_digitada == defesa_exigida[:len(palavra_digitada)]:
            if palavra_digitada == defesa_exigida:
                if defesa_exigida == 'contra-ataque':
                    print_slow(f'{contra} Você causou {dano} de dano!',0.02)
                    vida_inimigo-=dano
                    break
                else:
                    print_slow(random.choice(defendeu),0.02)
                    break
        else:
            print_slow(f'{random.choice(sofreu)} Você recebeu {dano} de dano.',0.02)
            vida_player-=dano
            break
