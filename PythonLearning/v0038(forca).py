secreto = 'joao'
digitadas = [ ]
count = 5

while True :
	tentativa = input('Digite uma letra: ')
	if len(tentativa) > 1:
		print('Vc ó pode digitar UMA letra...')
		continue
	digitadas.append(tentativa)
	
	if tentativa in secreto:
		print(f'\nUHUUUUL a letra {tentativa} está na palavra secreta!!')
	else:
		print(f'\nPuts, a letra {tentativa} NÃO está na palavra secreta...')
		digitadas.pop()
		count -= 1
		
	secreta_temp = ' '
	for letra_temp in secreto:
		if letra_temp in digitadas:
			secreta_temp += letra_temp
		else:
			secreta_temp += '*'
	if secreta_temp == secreto:
		print(f'PARABENS, vc conseguiu descobrir a palavra secreta!!! ({secreto})')
		break
	else:
		print(f'\n{secreta_temp}\nChances restantes: {count}\n')
	
	if count == 0:
		print(' Infelizmente suas chances acabaram, vc PERDEU...')
		break
	else:
		continue
