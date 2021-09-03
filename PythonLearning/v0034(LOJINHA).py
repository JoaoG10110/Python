print('-=-'*15)
print('             LOJINHA DO SEU JOÃO')
print('-=-'*15)
print(' ')
print('INVENTÁRIO')
print(' ')
print('[1] MODELO 1 128GB \nR$3.300,00')
pitem1 = 3300
print(' ')
print('[2] MODELO 2 512GB \nR$7.500,00')
pitem2 = 7500
print(' ')
print('[3] MODELO 3 256GB \nR$5.400,00')
pitem3 = 5400
print(' ')
item = int(input('Digite o número do produto que deseja comprar: '))
print(' ')
if item == 1:
	print('Valor do produto: R$3.300,00')
	print(f'Escolha uma forma de pagamento \n[1] À vista (Boleto) - 10% de desconto - R${pitem1-(0.1*pitem1):.2f} \n \n[2] À vista (Cartão de Débito) - 5% de desconto - R${pitem1-(0.05*pitem1):.2f} \n \n[3] Parcelado (Cartão de Crédito) - 2x sem juros ou 20% de juros em 3x ou mais.')
	print(' ')
	fp = int(input('DIGITE O NÚMERO RELACIONADO À FORMA DE PAGAMENTO: '))
	if fp == 3:
		parcelas = int(input('Em quantas parcelas você deseja pagar? '))
		if parcelas == 2:
			print(f'O valor total da compra é de R${pitem1:.2f}')
		else:
			print(f'O pagamento será feito em {parcelas}x de R${(pitem1+(0.2*pitem1))/parcelas:.2f}')
	elif fp == 2:
		print(f'O valor total da compra é de R${pitem1-(0.05*pitem1):.2f}')
	elif fp == 1:
		print(f'O valor total da compra é de R${pitem1-(0.1*pitem1):.2f}')
elif item == 2:
	print('Valor do produto: R$7.500,00')
	print(f'Escolha uma forma de pagamento \n[1] À vista (Boleto) - 10% de desconto - R${pitem2-(0.1*pitem2):.2f} \n \n[2] À vista (Cartão de Débito) - 5% de desconto - R${pitem2-(0.05*pitem2):.2f} \n \n[3] Parcelado (Cartão de Crédito) - 2x sem juros ou 20% de juros em 3x ou mais.')
	print(' ')
	fp = int(input('DIGITE O NÚMERO RELACIONADO À FORMA DE PAGAMENTO: '))
	if fp == 3:
		parcelas = int(input('Em quantas parcelas você deseja pagar? '))
		if parcelas == 2:
			print(f'O valor total da compra é de R${pitem2:.2f}')
		else:
			print(f'O pagamento será feito em {parcelas}x de R${(pitem2+(0.2*pitem2))/parcelas:.2f}')
	elif fp == 2:
		print(f'O valor total da compra é de R${pitem2-(0.05*pitem2):.2f}')
	elif fp == 1:
		print(f'O valor total da compra é de R${pitem2-(0.1*pitem2):.2f}')
elif item == 3:
	print('Valor do produto: R$5.400,00')
	print(f'Escolha uma forma de pagamento \n[1] À vista (Boleto) - 10% de desconto - R${pitem3-(0.1*pitem3):.2f} \n \n[2] À vista (Cartão de Débito) - 5% de desconto - R${pitem3-(0.05*pitem3):.2f} \n \n[3] Parcelado (Cartão de Crédito) - 2x sem juros ou 20% de juros em 3x ou mais.')
	print(' ')
	fp = int(input('DIGITE O NÚMERO RELACIONADO À FORMA DE PAGAMENTO: '))
	if fp == 3:
		parcelas = int(input('Em quantas parcelas você deseja pagar? '))
		if parcelas == 2:
			print(f'O valor total da compra é de R${pitem3:.2f}')
		else:
			print(f'O pagamento será feito em {parcelas}x de R${(pitem3+(0.2*pitem3))/parcelas:.2f}')
	elif fp == 2:
		print(f'O valor total da compra é de R${pitem3-(0.05*pitem3):.2f}')
	elif fp == 1:
		print(f'O valor total da compra é de R${pitem3-(0.1*pitem3):.2f}')
