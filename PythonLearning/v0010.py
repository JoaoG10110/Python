print('='*23)
print('Calculadora de desconto')
print('='*23)
po = float(input('Qual o preço do produto? R$'))
d = float(input('Qual a porcentagem de desconto? '))
pd = float(po-(po*(d/100)))
print(f'O valor do produto com desconto é R${pd:.2f}')
