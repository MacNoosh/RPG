from funcoes import *
from funcoes import print_slow
from mecanicas_jogador import *
import mecanicas_jogador
import time
import keyboard
import random
#import emoji


def historia():
    print_slow("""
    Depois anos de lealdade e serviço ao seu reino, o cavaleiro Bravmo'or enfrentou uma traição devastadora que o levou a uma jornada sombria, consumido pela dor e pela escuridão, 
    ele se entregou ao poder da morte em busca de vingança. Como cavaleiro da morte, ele ceifou vidas sem propósito, perdido em um ciclo de destruição.Seu desejo de transformar a 
    terra em um mundo das trevas o consumiu, espalhando desespero e destruição por onde passava. Seu nome tornou-se sinônimo de medo e terror, enquanto ele mergulhava o mundo em um 
    abismo de desolação. Apesar dos lampejos de humanidade que ainda ecoavam dentro dele, o cavaleiro continuou em sua cruzada sombria,cada vez mais mergulhado na escuridão.Seus atos 
    de crueldade e opressão tornaram-se ainda mais brutais, alimentando-se do poder que ele tanto desejava. Assim, ascendeu ao poder, Dreadmo'or!

    No pátio do castelo, a infantaria dos que marcham para combater a dominação do cavaleiro da morte, Dreadmo'or, treinam incansavlmente. Em um momento, você se pega pensando em todos
    os acontecimentos que culminaram para essa situação, nesse momento você sente cheiro de sangue... você se distraiu na hora do treinamento, REAJA!
               DIGITE CORTE PARA ATACAR / FINTA PRA DEFENDER / DIRECIONAIS PARA DESVIAR""",0.048)

    #tutorial_desvio(3)
      

    print_slow("""Após o treinamento, o esquadrão de batedores do reino trazem péssimas notícias, um dos exército de Dreadmo'or marcha para atacar um dos poucos bastiões que sobraram 
    no mundo, a cidade de LUMINARA. O rei, Leothan "O Dourado", rapidamente convoca seus generais, recrutando todos os guardas reais da cidade. 

    A caminho para a defesa das muralhas da cidade, um antigo mago do reino chamado Galadran Sussurroestelar te observa fixamente, você escolhe deixar de lado e preparar-se para 
    eventual batalha contra o exército de Dreadmo'or.

    O ataque começa no cair da noite, após horas de uma batalha sangrenta, o exército do cavaleiro da morte parece nunca acabar. A tropa de Dreadmo'or consegue se infiltrar dentro da
    da cidade de Luminara, todos sob o comando de Leothan voltam para o castelo para tentar defende-lo. Depois de chegar nos portões do castelo e viscerar mais uma criatura do exército 
    inimigo, você percebe uma aura pesada no campo de batalha, uma aura emanando sede de poder e sangue, o próprio Dreadmo'or estava ali. O ascendido avança ferozmente ao castelo, você 
    vendo seus companheiros de batalha caindo um por um, em um ato de depesero, você avança em direção a Dreadmo'or. Após uma tentativa de golpe falha, o cavaleiro da morte desfere um 
    golpefatal. A diferença de força é discrepante...Você vê sua visão desvaindo.................aos poucos....................escuro....................................................
    ..................MORTE...................................................................................LUZ? Sua visão volta, você não está mais no campo de batalha, o lugar te
    conforta de certa maneira, você sente seu corpo leve e escuta uma voz no fundo, dizendo: "Que a luz dourada da esperança brilhe incessantemente em teu caminho, guiando-te através 
    das sombras do ascendido. 
    Que a tua alma seja banhada por essa luz divina, lembrando-te de que a esperança é a palavra que nunca se apaga.". Após as palavras da desconhecida, você 
    volta a vida no campo de batalha, ensanguentado e com pouca força vital, algo dentro de você grita!!!""",0.048)

    #esperança(3)

    print_slow(""" Você tenta gritar algo mas apenas sai um gemido inaudível. Quase desmaindo novamente você ainda consegue acompanhar o que vinha a seguir na batalha, por algum motivo, depois 
        da sua ressureição, Dreadmo'or parecia enfraquecido. Galadran Sussurroestelar emerge, e em um dialeto estranho, fala algo sonoramente parecido com sagrado. Após a fala de Galadran
        uma explosão de luz recai sobre a cidade e o cavaleiro da morte dá a ordem de retirada para seu exército.
     
        Você acorda no acampamento dos feridos, ainda um pouco desnorteado ainda, você vê a figura embaçada de uma silueta familiar de um senhor com barba e cabelos brancos, ele te 
        observa fixamente por alguns minutos e pergunta:
        """,0.048)
    
    nome_player = input('Você se lembra do seu nome, jovem guarda?')
    nome_do_jogo = 'Elder {Str}ing'
    

    print_slow(f""" Você tenta lembrar do seu nome, e com um pouco de dificuldade você fala {nome_player}. Depois de sua consciência voltar ao normal, você pouco a pouco lembra de todo
    desenrolar da batalha. O senhor de barba e cabelos grisalhos era nada mais que Galadran. O mago do reino então curioso lhe faz uma pergunta: " {nome_player}, você viu o sol? sentiu
    a luz?" Você acena com a cabeça, lembrando das palavras da voz que ouvira. Logo em seguida Galadran continua em um tom sério: "Isso pode ser vital para a derrocada de Dreadmo'or,
    o que vou lhe contar é um costume antigo, em que os abeçoados pelos Deuses conseguem utilizar. Aparentemente você foi abençoado pela mesma Deusa que eu, o nome dela é Solistra, a 
    Deusa do sol e da luz. A prática herdada dos Deuses são as palavras de conhecimento, ou se você quiser chamar, as {nome_do_jogo}. Essas palavras podem ser adquiridas durante sua 
    vida mas nem todos percebem o seu significado apenas os afortunados." Você sem entender como entrou nessa armadilha do destino fica aterrorizado, quando pulou para desferir o golpe
    em Dreadmo'or foi pela pura emoção do momento da batalha, agora você terá que enfretar o mal de frente. Galadran continua: " {nome_player} não tema jovem guarda, da mesma maneira
    que Solistra nos dá responsabilidade nos dá poder, amanhã cedo partiremos em busca de Dreadmo'or." Você ainda impactado do que acontecera, mal consegue dormir, mas o cansaço lhe
    vence.

    No dia seguinte Galadran lhe espera no portão, explica que a melhor hora para tentar uma investida seria nesse momento que o cavaleiro da morte está enfraquecido, dando duas 
    opções de caminho para seguir até a Fortaleza do Desespero sendo eles, a Floresta dos Sussuros Antigos ou a Cordilheira das Chamas Devoradoras. Logo em seguida você pensa e fala:
        """,0.048)
    


#DIVISÃO DOS CAMINHOS



    caminho = input('Cordilheira ou Floresta?').upper()
    while caminho not in ['CORDILHEIRA', 'FLORESTA']:
        caminho = input('Cordilheira ou Floresta?').upper()
        
    if caminho == 'FLORESTA':
        print_slow(f"""Logo após a sua escolha do seu destino, o mago fala que irá pela Cordilheira das chamas devoradoras, que cada caminho há pelo menos 2 Generais de Dreadmo'or e que cada 
            um deles foi almadioçoada com um pedaço da alma do cavaleiro da morte, cabe a vocês dois enfraquece-lo ainda mais para obter mais chances de sucesso. Depois de um breve aceno,
            o Galadran o encoraja dizendo " {nome_player} chegando primeiro na Fortaleza, me espere!".

            Saindo pelo portão norte você se direciona para a Floresta dos Susurros Antigos, nela você é recepcionado por um dríade chamada Galatea e explica que trantando a floresta como
            merece, ela te recompensará com proteção. Acantha pede uma escolta até um cemtiério do seu antigo povo, você a escuta e aceita seu pedido.

            Seguindo pela estrada principal, vocês encotram o cemitério que Galatea havia mencionado. Você escuta um barulho estranho vindo das das catacumbas. 
            {nome_player} deseja investigar?""",0.048)
        
        resposta = input('Continuar? [S/N] ').upper()    
        while resposta not in 'SN':
            resposta = input('Continuar? [S/N] ').upper()
        
        if resposta == 'S':
            print_slow(f"""Você pede a Galatea que fique em segurança for invertigar o barulho, após um exploração rápida você encontra alguns mortos-vivos. {nome_player}deseja 
            enfrenta-los?""",0.048)
        
            resposta = input('Continuar? [S/N] (Digite Codex para ver sua lista de ataques.) ').upper()
            while True:
                if resposta == 'CODEX':
                    for palavra in palavras_atk.keys():
                        print(palavra, end = ' | ')      
                    resposta = input(f'\nContinuar? [S/N] (Digite codex para ver sua lista de ataques.) ').upper()
                if resposta in 'SN':
                    break

            if resposta == 'S':
                mecanicas_jogador.vida_player = 30
                mecanicas_jogador.vida_inimigo = 30
                
                batalha_comum('Grupo de Mortos-Vivos',8,5,10)
                aprendizado('impacto',3)
                
                print_slow(f"""Após derrotar o grupo de mortos-vivos, seu codex aprendeu uma nova palavra: IMPACTO. Você percebe que na verdade os mortos-vivos foram invocados por alguma coisa. Adentrando nas partes mais profundas da catacumbas 
                você sente um poder sombrio, com cautela você se aproxima e se vê diante de um dos Generais de Dreadmo'or, Necroth o Senhor da Sepultura. {nome_player} PREPARE-SE""",0.048)
                mecanicas_jogador.vida_player = 35
                mecanicas_jogador.vida_inimigo = 50
                batalha_miniboss('Necroth',9,4,9) # mudar para batalha_miniboss
                
                
        print_slow(f"""Continuando pela estrada da floresta você chega a cidade élfica de Thalassëa, após uma rápida verificação nos portões, o acesso a cidade é liberado. Um clima de
                desconfiança paira sobre a cidade. Conversando com os comerciantes, você descobre que há relatos de furtos e como os elfos estão fazendo frente contra o exército do cavaleiro da
                morte os ladrões se aproveitam da impunidade. Após a explicação os comerciante suplicam por ajuda, {nome_player} dejesa ajuda-los?
                """,0.048)
        
        resposta = input('Continuar? [S/N] (Digite Codex para ver sua lista de ataques.) ').upper()
        while True:
            if resposta == 'CODEX':
                for palavra in palavras_atk.keys():
                    print(palavra, end = ' | ')      
                resposta = input(f'\nContinuar? [S/N] (Digite codex para ver sua lista de ataques.) ').upper()
            if resposta in 'SN':
                break
        
        if resposta == 'S':
            print_slow(f"""Pegando informações nos suburbios da cidade você toma ciência que o grupo de ladrões encontram-se dentro de uma caverna aos arredores da cidade, entrando na 
                    caverna você se depara com um grupo de 4 ladrões, PREPARE-SE!""",0.048)
            mecanicas_jogador.vida_player = 45
            mecanicas_jogador.vida_inimigo = 50
            batalha_comum('Gangue de Bandidos',10,5,9)
            aprendizado('estocada',4)
        
        print_slow(f"""Após derrotar a gangue de banidos, seu codex aprendeu uma nova palavra: ESTOCADA. Saindo da cidade de Thalassëa, prosseguindo por mais alguns dias, você se depara com um templo antigo. Aproximando-se um pouco mais percebe que há um tabuleta
                    de mármore que tinha gravado em si a seguinte frase: "Santuário da Eterna Renovação". Um pouco contraditório, já que você percebe que ao redor do templo há muita vegetação em 
                    estado de putrefação. Você deseja adentrar no templo, {nome_player}?""",0.048)
        
        resposta = input('Continuar? [S/N] (Digite Codex para ver sua lista de ataques.) ').upper()
        while True:
            if resposta == 'CODEX':
                for palavra in palavras_atk.keys():
                    print(palavra, end = ' | ')      
                resposta = input(f'\nContinuar? [S/N] (Digite codex para ver sua lista de ataques.) ').upper()
            if resposta in 'SN':
                break
        
        if resposta == 'S':
            print_slow(f"""Aos poucos você vai se aprofundando dentro do templo e começa a entender a quem um dia pertenceu, as próprias paredes contam a sua história, esse templo 
                        pertencia aos Druidas e servia para a manutenção e equilibrio da floresta em volta dele. Chegando mais perto do salão principal você sente o cheiro de putrefação ainda mais 
                        forte, na antesala nota-se um corpo semi-devorado de um animal e logo em seguida um Urso Corrompido, você deseja enfrenta-lo {nome_player}? """,0.048)
        
            resposta = input('Continuar? [S/N] (Digite Codex para ver sua lista de ataques.) ').upper()
            while True:
                if resposta == 'CODEX':
                    for palavra in palavras_atk.keys():
                        print(palavra, end = ' | ')      
                    resposta = input(f'\nContinuar? [S/N] (Digite codex para ver sua lista de ataques.) ').upper()
                if resposta in 'SN':
                    break
            
            if resposta == 'S':
                mecanicas_jogador.vida_player = 50
                mecanicas_jogador.vida_inimigo = 50
                batalha_comum('Urso Corrompido',12,5,9)
                print_slow(f"""Após derrotar o urso corrompido, seu codex aprendeu uma nova palavra: ARREMESSO. O caminho para a sala principal está aberto e você já presume do que está adiante é um dos Generais de Dreadmo'or. {nome_player}, prepare-se!""",0.048)
                aprendizado('arremesso',5)
                
                
                mecanicas_jogador.vida_player = 55
                mecanicas_jogador.vida_inimigo = 70
                batalha_miniboss('General Mortanis',15,4,9) # mudar para miniboss
                aprendizado('esmagamento',7)
        
        print_slow(f"""Após derrotar o General Mortanis, seu codex aprendeu uma nova palavra: ESMAGAMENTO. Quanto mais próximo da Fortaleza do Desespero, você percebe um estado de putrefação avançado na floresta no qual a transformou num grande pântano. O cheiro era
                        insuportável, você não via a hora de sair daquele lugar insalubre, derrepente você nota um vulto passandos entre as árvores, e pergunta a si mesmo que tipo de ser 
                        viveria naquelas condições, {nome_player} deseja seguir o vulto? """,0.048)
        
        resposta = input('Continuar? [S/N] (Digite Codex para ver sua lista de ataques.) ').upper()
        while True:
            if resposta == 'CODEX':
                for palavra in palavras_atk.keys():
                    print(palavra, end = ' | ')      
                resposta = input(f'\nContinuar? [S/N] (Digite codex para ver sua lista de ataques.) ').upper()
            if resposta in 'SN':
                break
        
        if resposta == 'S':
            print_slow(f"""Com curiosidade você vai em busca da resposta e seguindo adiante encontra uma cabana cheia de limo e fungos pelas paredes, aparentemente a porta se encontrava
                            meio aberta e você não hesita em entrar nessa cabana. Com um relanse de olhar você já sabia qual criatura vivia ali, com caldeirões e restos mortais de animais, era óbivio ser
                            um covil de uma Bruxa. Quando já estava pronto para partir, tarde demais! Seu Codez aprenderá a palavra ROMPIMENTO {nome_player}, PREPARE-SE""",0.048)
            mecanicas_jogador.vida_player = 60
            mecanicas_jogador.vida_inimigo = 50
            batalha_comum('Bruxa',18,3.5,9)
            aprendizado('rompimento',6)    
            
    #CAVALEIRO DA MORTE - FIM DA FLORESTA
        
        print_slow("""Após percorrer um longo caminho você finalmente chega ao seu objetivo, a fortaleza do desespero de Dread'moor. Mantendo uma distância segura você observa o funcionamento 
            do castelo, quando abruptamente você sente uma presença vindo atrás de você, desembainhando rapidamente sua espada e indo ao encontro de uma garganta... familiar? Era 
            Galadran, impressionado ele fala: “Pelo visto a aventura fez melhor a você do que a mim”, logo em seguida você pede desculpas e o velho mago lhe dá um sorriso. Vocês 
            fazem uma breve reunião para escolher a melhor abordagem, Galadran define a melhor estratégia será ele limar os salões do castelo para você conseguir enfrentar o cavaleiro
            da morte. Após uma breve conversa, vocês partem em direção a fortaleza, Galadran chega massacrando as tropas que restaram no castelo limpando uma sala após a outra, mas 
            era perceptível que pela quantidade de mana utilizada ele não duraria muito tempo, utilizando os últimos resquícios de poder mágico ele se esgota na ante-sala de Dread'moor,
            ele vira pra você e fala: “Agora é a hora de um novo herói meu jovem, que a deusa lhe abençoe, boa sorte!” depois das palavras do mago antes de abrir a porta você sente o
            mal encarnado atrás delas, com um longo suspiro você abre a porta. De certa maneira parecia que o cavaleiro da morte já lhe esperava, o olhar dele te menospreza, mas ao 
            mesmo tempo Solistra lhe dava a benção, coragem e poder. Você sente seu corpo imbuído por luz sagrada, PREPARE-SE!""",0.048)
        mecanicas_jogador.vida_player = 70
        mecanicas_jogador.vida_inimigo = 100
        batalha_miniboss("Dread'moor", 25,3,8)
        creditos()
        input('Aperte qualquer botão para voltar ao menu...')
        iniciar_jogo()

            
    else:
        print_slow(f"""Logo após a sua escolha do seu destino, o mago fala que irá pela Floresta dos Susurros Antigos, que cada caminho há pelo menos 2 Generais de Dreadmo'or e que cada 
            um deles foi almadioçoada com um pedaço da alma do cavaleiro da morte, cabe a vocês dois enfraquece-lo ainda mais para obter mais chances de sucesso. Depois de um breve aceno,
            o Galadran o encoraja dizendo " {nome_player} chegando primeiro na Fortaleza, me espere!".

            Saindo pelo portão norte você se direciona para a Cordilheira das chamas devoradoras, nela você é recepcionado por um anão chamado Grimgar e explica que desbravar a cordilheira
            com a devida honra, ela te recompensará com poder. Grimgar pede uma ajuda até um mina, que num passado recente, era do seu povo. Você, até então, decide apenas acompanha-lo.

            Seguindo pela trilha principal, vocês encotram a mina que Grimgar havia mencionado. Deseja ajudar Grimgar?
        """,0.048)
        
        resposta = input('Continuar? [S/N] ').upper()    
        while resposta not in 'SN':
            resposta = input('Continuar? [S/N] ').upper()
        
        if resposta == 'S':
            print_slow(f"""Ao adentrar na mina escuta-se um barulho, chegando mais perto você percebe que é um grupo de orcs minerando. Deseja enfreta-los?
        """,0.048)
        
            resposta = input('Continuar? [S/N] ').upper()
            while resposta not in 'SN':
                resposta = input('Continuar? [S/N] ').upper()
            
            if resposta == 'S':
                mecanicas_jogador.vida_player = 30
                mecanicas_jogador.vida_inimigo = 30
                
                batalha_comum('Grupo de Orcs',8,5,10)
                aprendizado('impacto',4)
                print_slow(f"""Após derrotar o grupo de orcs, seu codex aprendeu uma nova palavra: IMPACTO. Você percebe que um deles ainda está vivo, após interroga-lo é revelado o que lhe espera adiante, um dos generais de Dreadmo'or, Zorgrak o Ogro.
                Deseja enfrenta-lo?
                """,0.048)
                mecanicas_jogador.vida_player = 30
                mecanicas_jogador.vida_inimigo = 50
                batalha_miniboss('Zorgrak',9,4,9) 

        print_slow(f"""Após deixar a mina você continua pela trilha da montanha por algumas noites, depois de alguns dias em um pedaço você nota um construção misteirosa. Deseja 
                   investigar?
                """,0.048)
        
        resposta = input('Continuar? [S/N] (Digite Codex para ver sua lista de ataques.) ').upper()
        while True:
            if resposta == 'CODEX':
                for palavra in palavras_atk.keys():
                    print(palavra, end = ' | ')      
                resposta = input(f'\nContinuar? [S/N] (Digite codex para ver sua lista de ataques.) ').upper()
            if resposta in 'SN':
                break
        
        if resposta == 'S':
            print_slow(f"""Chegando mais perto você percebe que a construção nada mais era que um ninho de harpia. Prepare-se {nome_player}!
                """,0.048)
            mecanicas_jogador.vida_player = 35
            mecanicas_jogador.vida_inimigo = 50
            batalha_comum('Grupo de Harpias',10,5,9)
            aprendizado('estocada',5)
        
        print_slow(f"""Após derrotar o grupo de harpias, seu codex aprendeu uma nova palavra: ESTOCADA. Subindo ainda mais você chega no vilarejo Lume da Montanha, a população local parece surpresa com sua presença. Conversando com os locais eles falam que as visitas
            diminuiram consideravelmente devido ao aumento de ataque de monstros no vilarejo e que gerealmente eles acontecem a noite. Você deseja passar a noite {nome_player}?""",0.048)
        
        resposta = input('Continuar? [S/N] (Digite Codex para ver sua lista de ataques.) ').upper()
        while True:
            if resposta == 'CODEX':
                for palavra in palavras_atk.keys():
                    print(palavra, end = ' | ')      
                resposta = input(f'\nContinuar? [S/N] (Digite codex para ver sua lista de ataques.) ').upper()
            if resposta in 'SN':
                break
        
        if resposta == 'S':
            print_slow(f"""No meio da noite você acorda com grunidos, após olhar pela janela da pousada dois javalis da montanha estão atacando a cidade, deseja ajudar {nome_player}?
                       """,0.048)
        
            resposta = input('Continuar? [S/N] (Digite Codex para ver sua lista de ataques.) ').upper()
            while True:
                if resposta == 'CODEX':
                    for palavra in palavras_atk.keys():
                        print(palavra, end = ' | ')      
                    resposta = input(f'\nContinuar? [S/N] (Digite codex para ver sua lista de ataques.) ').upper()
                if resposta in 'SN':
                    break
            
            if resposta == 'S':
                mecanicas_jogador.vida_player = 35
                mecanicas_jogador.vida_inimigo = 50
                batalha_comum('Bando de Javalis',12,5,9)
                print_slow(f"""Após derrotar o bando de javalis, seu codex aprendeu uma nova palavra: ARREMESSO. Depois de aniquilar os dois javalis você pede mais informações sobre o que exatamente está acontecendo, um dos moradores que tinha mais conhecimento fala
                           que depois que sombras transformaram dia em noite no vilarejo as criaturas que tinham seu habitat um ponto mais alto perto do vilarejo começaram a aparecer.
                           Então você decide investigar, chegando perto do local aonde os javalis ficavam você sente um cheiro de putrefação e logo percebe o porque, haviam vários cadáveres
                           a maioria todos comidos, indo mais além, você encontra o motivo de tudo. Era um dos generais de Dreadmo'or, o dragão Typhorix. Prepare-se {nome_player}!
                       """,0.048)
                aprendizado('arremesso',6)
                
                
                mecanicas_jogador.vida_player = 40
                mecanicas_jogador.vida_inimigo = 70
                batalha_miniboss('Typhorix',15,4,9) # mudar para miniboss
                aprendizado('esmagamento',8)
        
        
        print_slow(f"""Após derrotar o Typhorix, seu codex aprendeu uma nova palavra: ESMAGAMENTO. Descendo a cordilheira rumo a Fortaleza do Desespero você nota que a natureza está fora do seu equilibrio, vulcões com atividade além do normal fazendo surgir rios de
                   lava, o que tornava a caminhada ainda mais difícil. Algum tempo depois você sente tremores estranhos vindo da sua esquerda mesclado com alguns gritos. Deseja investigar
                   {nome_player}?
                       """,0.048)
        
        resposta = input('Continuar? [S/N] (Digite Codex para ver sua lista de ataques.) ').upper()
        while True:
            if resposta == 'CODEX':
                for palavra in palavras_atk.keys():
                    print(palavra, end = ' | ')      
                resposta = input(f'\nContinuar? [S/N] (Digite codex para ver sua lista de ataques.) ').upper()
            if resposta in 'SN':
                break
        
        if resposta == 'S':
            print_slow(f"""Chegando ao epicentro dos tremores e ondem haviam os gritos percebe-se o que restou de alguns centauros que acabam de lutar com um gigante de lava, antes de você
                       percerber já tinha sido notado. Seu codex aprenderá a palavra ROMPIMENTO, Prepare-se {nome_player}!
                       """,0.048)
            mecanicas_jogador.vida_player = 45
            mecanicas_jogador.vida_inimigo = 50
            batalha_comum('Gigante de Lava',18,3.5,9)
            aprendizado('rompimento',7)    
        
        print_slow("""Após percorrer um longo caminho você finalmente chega ao seu objetivo, a fortaleza do desespero de Dread'moor. Mantendo uma distância segura você observa o funcionamento 
            do castelo, quando abruptamente você sente uma presença vindo atrás de você, desembainhando rapidamente sua espada e indo ao encontro de uma garganta... familiar? Era 
            Galadran, impressionado ele fala: “Pelo visto a aventura fez melhor a você do que a mim”, logo em seguida você pede desculpas e o velho mago lhe dá um sorriso. Vocês 
            fazem uma breve reunião para escolher a melhor abordagem, Galadran define a melhor estratégia será ele limar os salões do castelo para você conseguir enfrentar o cavaleiro
            da morte. Após uma breve conversa, vocês partem em direção a fortaleza, Galadran chega massacrando as tropas que restaram no castelo limpando uma sala após a outra, mas 
            era perceptível que pela quantidade de mana utilizada ele não duraria muito tempo, utilizando os últimos resquícios de poder mágico ele se esgota na ante-sala de Dread'moor,
            ele vira pra você e fala: “Agora é a hora de um novo herói meu jovem, que a deusa lhe abençoe, boa sorte!” depois das palavras do mago antes de abrir a porta você sente o
            mal encarnado atrás delas, com um longo suspiro você abre a porta. De certa maneira parecia que o cavaleiro da morte já lhe esperava, o olhar dele te menospreza, mas ao 
            mesmo tempo Solistra lhe dava a benção, coragem e poder. Você sente seu corpo imbuído por luz sagrada, PREPARE-SE!""",0.048)
        mecanicas_jogador.vida_player = 55
        mecanicas_jogador.vida_inimigo = 100
        batalha_miniboss("Dread'moor", 25,3,8)
        creditos()
        input('Aperte qualquer botão para voltar ao menu...')
        iniciar_jogo()




          