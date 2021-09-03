v = int(input('Digite a velocidade do carro: '))
vl = int(80)
if v > vl:
	m = float((v-vl)*7)
	print(f'Você ultrapassou o limite de velocidade e deverá pagar uma multa de R${m:.2f}')
else:
	print('Você não ultrapassou o limite de velocidade, parabéns!')
