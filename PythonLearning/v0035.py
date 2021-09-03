from random import randint
from time import sleep
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
p1 = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print(' ')
print('-=-'*11)
print(f'O Computador escolheu {opcoes[pc]}.')
print(f'O Jogador escolheu {opcoes[p1]}.')
print('-=-'*11)
print(' ')
if pc == 0:
	if p1 == 0:
		print('EMPATE')
	elif p1 == 1:
		print('Você GANHOU')
	elif p1 == 2:
		print('Você PERDEU')
	else:
		print('JOGADA INVÁLIDA')
elif pc == 1:
	if p1 == 0:
		print('Você PERDEU')
	elif p1 == 1:
		print('EMPATE')
	elif p1 == 2:
		print('Você GANHOU')
	else:
		print('JOGADA INVÁLIDA')
elif pc == 2:
	if p1 == 0:
		print('Você GANHOU')
	elif p1 == 1:
		print('Você PERDEU')
	elif p1 == 2:
		print('EMPATE')
	else:
		print('JOGADA INVÁLIDA')
