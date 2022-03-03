while True:
	cpf = input('Digite o CPF: ')
	reverso = 10
	novo_cpf = cpf[:-2]
	soma = 0
	
	for i in range(19):
		if i > 8:
			i -= 9
	
		soma += int(novo_cpf[i]) * reverso
		reverso -= 1
	
		if reverso < 2:
			reverso = 11
			d = 11 - (soma % 11)
	
			if d > 9:
				d = 0
			soma = 0
			novo_cpf += str(d)
	
	sequencia = novo_cpf == str(novo_cpf[0]) * 11
	
	if cpf == novo_cpf and not sequencia:
		print('CPF Válido\n')
	else:
		print('CPF Inválido\n')



