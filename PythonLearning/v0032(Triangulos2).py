print('Dê 3 medidas para verificar se é possível formar um triângulo com elas.')
a = float(input('Primeira medida: '))
b = float(input('Segunda medida: '))
c = float(input('Terceira medida: '))
if a + b > c and a + c > b and b + c > a:
	print('SIM!! É possível fazer um triângulo.')
	if a==b and b==c:
		print('Será formado um triângulo EQUILÁTERO.')
	elif a==b or a==c or b==c:
		print('Será formado um triângulo ISÓSCELES.')
	elif a!=b and b!=c:
		print('Será formado um triângulo ESCALENO.')
else:
	print('NÃO!! Não é possível fazer um triângulo com essas medidas...')
