print('\033[32m-=-\033[m'*15)
print('             \033[1;32mEMPRÉSTIMO BANCÁRIO')
print('\033[32m-=-\033[m'*15)
print()
vc = float(input('Qual o valor da casa? R$'))
s = float(input('Qual o seu salário mensal? R$'))
t = int(input('Em quantos anos você pretende pagar? '))
prestacaom = float(vc/(t*12))
if prestacaom <= (0.3*s):
	print('\033[1;32mPARABÉNS!!\033[m\033[32m O seu empréstimo foi \033[1;32mAPROVADO\033[m.')
	print(f'O financiamento será de \033[32mR${prestacaom:.2f}/mês\033[m, e será quitado em {t*12} meses.')
else:
	print('Desculpa, mas o seu empréstimo foi \033[1;4;31mNEGADO\033[m.')
