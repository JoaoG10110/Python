from datetime import date
data = int(input('Qual o ano do seu nascimento? '))
atual = date.today().year
idade = atual-data
if idade <=9:
	print(f'Você tem {idade} anos, é um atleta MIRIM.')
elif 9<idade<15:
	print(f'Você tem {idade} anos, é um atleta INFANTIL.')
elif 13<idade<20:
	print(f'Você tem {idade} anos, é uma atleta JUNIOR.')
elif 18<idade<21:
	print(f"Você tem {idade} anos, é um atleta SÊNIOR.")
elif idade>20:
	print(f'Você tem {idade} anos, é um atleta MASTER.')
