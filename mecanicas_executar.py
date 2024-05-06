import random


def executar_mecanicas():
    from mecanicas_boss import mecanica_1, mecanica_2, mecanica_3, mecanica_4, mecanica_5, mecanica_6
    todas_mecanicas = [mecanica_1, mecanica_2, mecanica_3, mecanica_4, mecanica_5, mecanica_6]
    for mecanica in todas_mecanicas:
        mecanica(timeout=random.randint(2, 3))