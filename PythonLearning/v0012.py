d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input(f'Quantos Km foram percorridos durante os {d} dias? '))
print(f'O total a pagar é R${(d*60)+(km*0.15):.2f}')
