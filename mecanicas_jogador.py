import time
import keyboard
from colorama import Fore, Back, Style, init
from funcoes import *
import random



palavras_atk = {'corte': 2}
palavras_dfs_totais = {'corte': 'resistencia', 'impacto': 'proteçao', 'estocada': 'esquiva', 'arremesso': 'bloqueio', 'rompimento': 'finta', 'esmagamento': 'contra-ataque'}
palavras_dfs_player = {'corte': 'resistencia'}

vida_player = vida_inimigo = 30

vida_miniboss1 = 50
vida_miniboss2 = 70

vida_boss = 100



def aprendizado(palavra, dano):
    palavras_atk[palavra] = dano
    for key in palavras_dfs_totais:
        if key in palavras_atk:
            palavras_dfs_player[key] = palavras_dfs_totais[key]

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
    frases = ['\nVocê vê uma abertura. É sua vez de atacar! ',
              f'\nO {inimigo} está vulnerável! Aproveite sua chance! ',
              '\nVocê sente a adrenalina. Qual é sua ação? ', 'Agora é com você! Prepare-se para atacar: ']
    
    errou = [f'\nInfelizmente, seu ataque não encontra o {inimigo}.',
             f'\nSeu ataque falha, deixando o {inimigo} ileso.',
             f'\nApesar de seus esforços, você não consegue acertar o {inimigo}.',
             f'\nSeu golpe passa raspando, mas não acerta o {inimigo}.']
    
    demorou = [f'\nVocê hesita por um momento e perde sua oportunidade de agir. O que permitiu que o {inimigo} lhe golpeasse, causando ',
               f'\nSua hesitação permite ao {inimigo} agir antes de você, e lhe causar',
               f'\nSua indecisão custa caro, e o {inimigo} aproveita a chance, causando ']
    
    tempo_inicial = time.time()
    print_slow(random.choice(frases),0.02)
    acao = input('')
    
    while True:
        tempo_final = time.time() - tempo_inicial

        if tempo_acao <= tempo_final:
            print_slow(f'{random.choice(demorou)}, {dano} de dano',0.02)
            vida_player -= dano
            break
        
        else:
            if acao in palavras_atk:
                acerto = round(palavras_atk[acao] * 2 * (tempo_acao - tempo_final))
                acertou = [f'\nVocê desfere um {acao.upper()} certeiro!',
                           f'\nVocê desfere um {acao.upper()} devastador no {inimigo}!',
                           f'\nSeu {acao.upper()} encontra {inimigo} com precisão!']
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
    
    frases = [f'\nSeus instintos alertam você sobre o ataque iminente do {inimigo}. Rápido! Use: {defesa_exigida.upper()}\n', 
              f'\nO {inimigo} faz um movimento agressivo em sua direção. Será necessário {defesa_exigida.upper()}\n',
              f'\nO {inimigo} lança um olhar de desafio em sua direção, pronto para testar sua {defesa_exigida.upper()}.\n',
              f'\nO som de passos pesados ecoa ao seu redor, anunciando a investida iminente do {inimigo}. É hora de mostrar sua {defesa_exigida.upper()}!\n']
    print_slow(random.choice(frases),0.02)
    
    defendeu = [f'\nVocê antecipa os movimentos do {inimigo} com uma precisão impressionante, bloqueando seu ataque com um {defesa_exigida} rápido e eficaz!\n',
                f'\nVocê se move com uma graça surpreendente, desviando habilmente do ataque do {inimigo}. Sua {defesa_exigida} é impecável!\n']
    contra = f'\nCom um movimento fluído, você desvia o ataque do {inimigo}, transformando seu ímpeto ofensivo em uma oportunidade de contra-ataque. Sua defesa não só protege, mas também surpreende!\n'
    
    sofreu = [f'\nO golpe do {inimigo} encontra seu caminho através de suas defesas, deixando uma sensação de impacto brutal em seu corpo.\n',
              f'\nVocê é pego desprevenido pelo ataque do {inimigo}, que encontra sua brecha.\n',
              f'\nVocê se vê cercado pela dor do ataque do {inimigo}, que parece encontrar uma fraqueza em suas defesas e explorá-la ao máximo.\n']
    
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

def batalha_comum(inimigo,dano, tempo_atk, tempo_dfs):
    global vida_inimigo
    global vida_player


    while True:
        atacar(tempo_atk,inimigo,dano)
        
        if vida_inimigo > 0:
            defender_2(tempo_dfs,inimigo,dano)
        
        limpa_linha()
        print(f'Vida Player: {vida_player}\nVida Inimigo: {vida_inimigo}')
        
        if vida_player <= 0:
            print('perdeu')
            break
        
        if vida_inimigo <= 0:
            print('venceu. ir pra próxima.')
            vida_player = vida_inimigo = 30  
            break   
        
    