import time
import keyboard
from colorama import Fore, Back, Style, init
from funcoes import *
import random

palavras_atk = {'corte': 2}
palavras_dfs_totais = {'corte': 'resistencia', 'impacto': 'proteçao', 'estocada': 'esquiva', 'arremesso': 'bloqueio', 'rompimento': 'finta', 'esmagamento': 'contra-ataque'}
palavras_dfs_player = {'corte': 'resistencia'}

vida_player = vida_inimigo = 30


def aprendizado(palavra, dano):
    palavras_atk[palavra] = dano
    for key in palavras_dfs_totais:
        if key in palavras_atk:
            palavras_dfs_player[key] = palavras_dfs_totais[key]

def tutorial_atk(tempo):
    tempo_inicial = time.time()
    palavra = input('Diga a palavra de ataque que você aprendeu até agora, CORTE:  ')
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
    palavra = input('Agora vamos treinar sua defesa, diga a palavra de defesa que você aprendeu RESISTENCIA: ')
    while True:
        tempo_final = time.time() - tempo_inicial
        if tempo_final >= tempo:
            print(f'Demorou muito ({tempo_final:.1f} segundos)! Diga mais rápido!')
            tutorial_defesa(tempo)
            break
        elif tempo_final < tempo and palavra == 'resistencia':
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

def carta():
    global vida_inimigo
    global vida_player
    
   
    ataques = ['corte', 'impacto', 'estocada', 'arremesso', 'rompimento', 'esmagamento']
    defesas = ['resistencia', 'proteçao', 'esquiva', 'bloqueio', 'finta', 'contra-ataque']
    
    escolha = input('''
Escolha sua carta:
 ______
|      |    
|      |
|ATAQUE| 
|      |
|______|
   ou
 ______
|      |
|      |
|DEFESA|
|      |
|______|

''').lower()
    while escolha not in 'ataquedefesa':
            escolha = input('''
Escolha sua carta:
 ______
|      |    
|      |
|ATAQUE| 
|      |
|______|
   ou
 ______
|      |
|      |
|DEFESA|
|      |
|______|

''').lower()
        
    if escolha == 'ataque':
        player = random.choice(ataques)
        inimigo = random.choice(defesas)
        print_slow(f'Você tirou a carta de {player.upper()} | PODER: {len(player)}.\nO inimigo tirou a carta de {inimigo.upper()}. | PODER: {len(inimigo)}',0.04)
       
        
    else:
        player = random.choice(defesas)
        inimigo = random.choice(ataques)
        print_slow(f'Você tirou a carta de {player.upper()} | PODER: {len(player)}.\nO inimigo tirou a carta de {inimigo.upper()}. | PODER: {len(inimigo)}',0.04)

    
    dano_carta = (len(player) - len(inimigo))*2
    if dano_carta < 0:
        print_slow(f'\nVocê recebeu {dano_carta} de dano.',0.04)
        vida_player -= dano_carta
    if dano_carta == 0:
        print_slow(f'\nEmpate!',0.04)
    else:
        print_slow(f'\nVocê causou {dano_carta} de dano.',0.04)
        vida_inimigo -= dano_carta

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
    print_slow(random.choice(frases),0.04)
    acao = input('')
    
    while True:
        tempo_final = time.time() - tempo_inicial

        if tempo_acao <= tempo_final:
            print_slow(f'{random.choice(demorou)}, {dano} de dano',0.04)
            vida_player -= dano
            break
        
        else:
            if acao in palavras_atk:
                acerto = round(palavras_atk[acao] * 2 * (tempo_acao - tempo_final))
                acertou = [f'\nVocê desfere um {acao.upper()} certeiro!',
                           f'\nVocê desfere um {acao.upper()} devastador no {inimigo}!',
                           f'\nSeu {acao.upper()} encontra {inimigo} com precisão!']
                print_slow(f'{random.choice(acertou)} causando {acerto} de dano',0.04)
                vida_inimigo-=acerto
                break
            elif acao not in palavras_atk:
                print_slow(random.choice(errou),0.04)
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
    print_slow(random.choice(frases),0.04)
    
    defendeu = [f'\nVocê antecipa os movimentos do {inimigo} com uma precisão impressionante, bloqueando seu ataque com um {defesa_exigida} rápido e eficaz!\n',
                f'\nVocê se move com uma graça surpreendente, desviando habilmente do ataque do {inimigo}. Sua {defesa_exigida} é impecável!\n']
    contra = f'\nCom um movimento fluído, você desvia o ataque do {inimigo}, transformando seu ímpeto ofensivo em uma oportunidade de contra-ataque. Sua defesa não só protege, mas também surpreende!\n'
    
    sofreu = [f'\nO golpe do {inimigo} encontra seu caminho através de suas defesas, deixando uma sensação de impacto brutal em seu corpo.\n',
              f'\nVocê é pego desprevenido pelo ataque do {inimigo}, que encontra sua brecha.\n',
              f'\nVocê se vê cercado pela dor do ataque do {inimigo}, que parece encontrar uma fraqueza em suas defesas e explorá-la ao máximo.\n']
    
    while True:
        tempo_final = time.time() - tempo_inicial
        
        if tempo_final > tempo_acao:
            print_slow(f'{random.choice(sofreu)} Você recebeu {dano} de dano.',0.04)
            vida_player-=dano
            break

        tecla = keyboard.read_event()
        if tecla.event_type == keyboard.KEY_DOWN and tecla.name in 'abcdefghijlmnopqrstuvxzkwyãê~^-ç':
            digitacao = tecla.name
            palavra_digitada += digitacao
            print(digitacao, end = '', flush=True)

        if palavra_digitada == defesa_exigida[:len(palavra_digitada)]:
            if palavra_digitada == defesa_exigida:
                if defesa_exigida == 'contra-ataque':
                    print_slow(f'{contra} Você causou {dano} de dano!',0.04)
                    vida_inimigo-=dano
                    break
                else:
                    print_slow(random.choice(defendeu),0.04)
                    break
        else:
            print_slow(f'{random.choice(sofreu)} Você recebeu {dano} de dano.',0.04)
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
            game_over()
            input('Aperte qualquer botão para voltar ao menu...')
            iniciar_jogo()
            break
        
        if vida_inimigo <= 0:
            break   

def batalha_miniboss(inimigo, dano, tempo_atk,tempo_dfs):
    global vida_inimigo
    global vida_player
    
    while True:
        
        opcoes = [
            lambda: atacar(tempo_atk, inimigo, dano),
            lambda: defender_2(tempo_dfs, inimigo, dano),
            lambda: carta()
        ]
        
        random.choice(opcoes)()
        
        limpa_linha()
        print(f'\nVida Player: {vida_player}\nVida Inimigo: {vida_inimigo}')
        
        if vida_player <= 0:
            game_over()
            input('Aperte qualquer botão para voltar ao menu...')
            iniciar_jogo()
            break
        
        if vida_inimigo <= 0:
            break         
