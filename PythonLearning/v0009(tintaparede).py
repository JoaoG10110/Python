print('='*31)
print('Calculadora de tinta pra parede')
print('='*31)
l = float(input('Insira a largura da parede em metros: '))
h = float(input('Insira a altura da parede em metros: '))
a = float(l*h)
at = float(2)
print(f'A área da parede é igual a: {a}m² \nPara pintar a parede, você precisará comprar {a/at} L de tinta.')
