import random
import time
import os
def tutorial_game():
    print("""
         .----.        .----.
DESVIAR:|  🢀   | ou   |  🢂   |  
         ------        ------
         .----.      .----.
ROLAR:  |  🡿   | ou |  🡾   |  
         ------      ------
         .----.     
PULAR:  |SPACE | 
         ------  
         .----.     
RECUAR: |  🢃   |
         ------    
         .----.      .----.
AGACHAR:|  🢃   | +  |  🢃   |  
         ------      ------        
          .----.     
DEFENDER:|  D   | 
          ------  
          .----.     
ATACAR:  |  A   | 
          ------ 
               .----.      .----.
CONTRA-ATACAR:|  D   | +  |  A   |  
               ------      ------     
        
          """)   
    
    
'''print_slow('teste',1)    
    
palavras_de_ataque = {'corte':1}
palavras_de_defesa = {'finta':8}

def atacar_tutorial():
    print_slow("""Este é o treinamento de ataque. Para atacar, diga as palavras de ataque que você já aprendeu o mais rápido que conseguir""",0.5)
   
    while True:
        tempo_inicial = time.time()
        ataque = input("Digite seu ataque: ")
        tempo_de_ataque = time.time() - tempo_inicial
        
        if tempo_de_ataque >= 4:
            print('Você demorou muito para agir, tente novamente.')
        
        elif ataque not in palavras_de_ataque:
            print(f'Você usou uma palavra sem efetividade. Tente novamente.')
        
        else:
            print(f'Legal! Você conseguiu usar o seu ataque em {tempo_de_ataque:.1f} segundos.')
            break
def defender_tutorial():
    print_slow("""Este é o treinamento de defesa. Para defender, diga as palavras de defesa que você já aprendeu o mais rápido que conseguir""",0.5)
   
    while True:
        tempo_inicial = time.time()
        defesa = input("Digite seu ataque: ")
        tempo_de_defesa = time.time() - tempo_inicial
        
        if tempo_de_defesa >= 4:
            print('Você demorou muito para agir, tente novamente.')
        
        elif defesa not in palavras_de_defesa:
            print(f'Você usou uma palavra sem efetividade. Tente novamente.')
        
        else:
            print(f'Legal! Você conseguiu se defender de um ataque em {tempo_de_defesa:.1f} segundos.')
            break'''
