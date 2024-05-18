from game import *
import random
import time
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
    
palavras_de_ataque = {'corte':1}
palavras_de_defesa = {'finta':8}

def atacar():
    print('Este é o treinamento de ataque. Para atacar, diga as palavras de ataque que você já aprendeu o mais rápido que conseguir')
    ataque = input("Digite seu ataque: ") 
    tempo_inicial = time.time()
    tempo_de_ataque = time.time() - tempo_inicial
    while tempo_de_ataque <= 4:
        if ataque not in palavras_de_ataque:
            print(f'Você usou uma palavra sem efetividade. Tente novamente.')
            tempo_inicial = time.time()   
            tempo_de_ataque = time.time() - tempo_inicial
            atacar()        
        else:
             print(f'Legal! Você ')

atacar()
