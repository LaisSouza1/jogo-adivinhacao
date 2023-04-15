#Jogo da adivinhação com a máquina

from random import randint
from time import sleep
pc = randint(0,5) #Faz computador pensar
print('\033[1;36m--*--' * 15)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar')
print('\033[1;36m--*--' * 15)
play = int(input('Em que número pensei?: ')) #Jogador tenta advinhar
print('\033[1;35mProcessando...')
sleep(2)
if play == pc:
    print('Parabéns você acertou o número secreto!')
else:
    print('Não foi dessa vez que você me venceu. Pensei no número {} e não no {}'.format(pc, play))
