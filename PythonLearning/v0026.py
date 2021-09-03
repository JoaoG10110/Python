print('Dê 3 medidas para verificar se é possível formar um triângulo com elas.')
a = float(input('Primeira medida: '))
b = float(input('Segunda medida: '))
c = float(input('Terceira medida: '))
if a + b > c and a + c > b and b + c > a:
	print('Sim!! É possível fazer um triângulo.')
else:
	print('NÃO!! Não é possível fazer um triângulo com essas medidas...')
