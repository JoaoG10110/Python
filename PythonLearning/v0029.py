from datetime import date
nasc = int(input('Em qual ano você nasceu? '))
atual = date.today().year
idade = int(atual - nasc)
if idade < 18:
	print(f'Você ainda tem {idade} anos, falta {18-idade} anos para você ter que ser alistar.')
elif idade == 18:
	print(f'Você tem ou vai fazer 18 anos, está na hora de você se alistar.')
elif idade > 18:
	print(f'Você já tem {idade} anos, devia ter se alistado a {idade-18} anos atrás.')
