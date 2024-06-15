from game import centralizar_texto

def tutorial_game():
    print(centralizar_texto("""
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
        
          """))   
    input()
   
