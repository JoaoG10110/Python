peso = float(input('Digite o seu peso (Kg): '))
alt = float(input('Dogite a sua altura (m): '))
imc = (peso/(alt*alt))
if 18.5>imc:
	print(f'Seu IMC é de {imc:.1f}, você está abaixo do peso.')
elif 18.5<=imc<=25:
	print(f'Parabéns, você está no peso ideial, seu IMC é de {imc:.1f}.')
elif 25<imc<30:
	print(f'Seu IMC é de {imc:.1f}, você está com sobrepeso.')
elif 30<=imc<=40:
	print(f'Seu IMC é de {imc:.1f}, você está com obesidade.')
elif 40<imc:
	print(f'Seu IMC é de {imc:.1f}, você está com obesidade mórbida.\nProcure um médico...')
