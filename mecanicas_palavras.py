import time
import random

dano = 1
dano_boss = 10
item = 1.5
vida_player = [20]
vida_boss = [50]

palavras_de_ataque = {'corte':1,'impacto':2,'estocada':3,'arremesso':4,'rompimento':5,'esmagamento':6}
palavras_de_defesa = {'finta':8,'bloqueio':9,'esquiva':10,'proteção':12,'resistência':15,'contra-ataque':6}

def atacar():
    print('turno de ataque')

    while True:
        tempo_inicial = time.time()
        ataque = input("Digite seu movimento: ")
        tempo_de_ataque = time.time() - tempo_inicial #fazer depois if tempo de digitacao > 4, dano é 0 
        dano_aleatorio = random.randint(1,5)

        if ataque not in palavras_de_ataque:
            vida_player.append(-dano_aleatorio)
            print(f'Você usou uma palavra sem efetividade. O inimigo retaliou!')
        elif tempo_de_ataque >= 4:
            print(f'Você demorou muito e seu ataque não surtiu efeito algum!')
        else:
            if dano_aleatorio == 5:
                dano_do_golpe = dano * item * palavras_de_ataque[ataque] *2 / tempo_de_ataque
                vida_boss.append(-dano_do_golpe)
                print(f'DANO CRÍTICO! Você acertou um belíssimo {ataque}, causando {dano_do_golpe:.1f}.')
            else:
                dano_do_golpe = dano * item * palavras_de_ataque[ataque] / tempo_de_ataque
                vida_boss.append(-dano_do_golpe)             
                print(f'Você acertou um {ataque}, causando {dano_do_golpe:.1f}.')

        break
    
def defender():
 
    print('TURNO DE DEFESA')

    while True:
        tempo_inicial = time.time()
        defesa = input("Digite seu movimento: ")
        tempo_de_defesa = time.time() - tempo_inicial
        if defesa == 'contra-ataque' and tempo_de_defesa <= 4 and defesa in palavras_de_defesa:
            dano_do_golpe = dano * item * palavras_de_defesa[defesa] / tempo_de_defesa
            vida_boss.append(-dano_do_golpe)
            print (f'Você usou um contra-ataque com sucesso e causou {dano_do_golpe:.1f} de dano!')

        elif tempo_de_defesa <= 4 and defesa in palavras_de_defesa:
            sucesso_defesa = dano_boss - (palavras_de_defesa[defesa] / (tempo_de_defesa*0.5))
            if sucesso_defesa < 0:
                print (f'Você conseguiu se defender a tempo e não tomou dano!')
            else:
                vida_player.append(-sucesso_defesa)
                print (f'Você conseguiu se defender a tempo e tomou {sucesso_defesa:.1f} de dano!')
        
        else:
            vida_player.append(-dano_boss)
            print(f'Você não conseguiu se defender do ataque e tomou {dano_boss} de dano!')
            

        break
    
while sum(vida_boss) > 0 or sum(vida_player) > 0:
    turno = random.randint(1,2)
    if turno == 1:
        atacar()
    else:
        defender()
        
    print(f'Vida atual player: {sum(vida_player):.1f}') # aqui vão entrar as barrinhas
    print(f'Vida atual boss: {sum(vida_boss):.1f}')

    if sum(vida_boss) <= 0:
        print('Jogador venceu')
        break
    elif sum(vida_player) <= 0:
        print('GAME OVER')
        break