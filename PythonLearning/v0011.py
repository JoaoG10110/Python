print('='*31)
print('Calculadora de aumento salarial')
print('='*31)
s = float(input('Qual o salário do funcionário? R$'))
pa = float(input('Qual a porcentagem de aumento? '))
sa = float(s+(s*(pa/100)))
print(f'O salário após o aumento será R${sa:.2f}')