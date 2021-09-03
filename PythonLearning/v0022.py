d = int(input('Qual a distância em Km da viagem? '))
pg = (d*0.5)
pp = (d*0.45)
if d <= 200:
	print(f'A viagem sairá R${pg:.2f}')
else:
	print(f'A viagem sairá R${pp:.2f}')
