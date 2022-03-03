num = input('Digite um número inteiro: ')
if num.isnumeric():
	num = int(num)
	if num % 2 == 0:
		print('O numero digitado é PAR.')
	else:
		print('O numero digitado é ÍMPAR.')
else:
	print("ERROR. O numero digitado nao é inteiro.")