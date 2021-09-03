city = str(input('Digite o nome de uma cidade: ')).title().strip().split()
print('Essa cidade tem "Santo" no nome? ', 'Santo' in city[0])
nome = str(input('Agora digite o seu nome: ')).title().strip()
print('Seu nome tem "Silva"? ', 'Silva' in nome)
