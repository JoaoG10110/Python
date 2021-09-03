salario = float(input('Qual o salário do funcionário? '))
if salario <= 1250:
	nsalario = (salario+(salario*0.15))
	print(f'Quem ganhava R${salario:.2f}, passa a ganhar R${nsalario:.2f}')
else:
	nsalario = (salario+(salario*0.10))
	print(f'Quem ganhava R${salario:.2f}, passa a ganhar R${nsalario:.2f}')
