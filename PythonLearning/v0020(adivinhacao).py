from random import randint
from time import sleep
npc = randint (0, 5)
print('Estou pensando em um número entre 0 e 5 \nTente adivinhar...')
nj = int(input('Em qual número eu pensei?'))
print('PROCESSANDO...')
sleep(2)
if npc == nj:
	print('PARABÉNS!! Você me venceu.')
else:
	print(f'ERROU!! Eu ganhei... Eu escolhi o número {npc}.')
