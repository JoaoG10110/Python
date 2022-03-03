nome = input('Qual o seu nome?')
print('Prazer, {}'.format(nome))
idade = input('Qual a sua idade?')
peso = input('Qual o seu peso?')
conf = str(input(f'{nome}, {idade} anos, {peso}Kg. Essas informações estão corretas?'))
if conf == sim:
	print(f'Obrigado por participar do teste, {nome}!!')
else:
	print('Por favor, insira novamente o seu mome.')
