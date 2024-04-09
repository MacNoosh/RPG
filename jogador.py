import time
import keyboard


def atack_1(timeout):
    print('Chegou a hora de provar ser um heroi, ataque!\n')
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



#teste