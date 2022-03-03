from  time import sleep
import emoji
print('DECOLAGEM DO FOGUETE PREPARADA')
sleep(1)
print('''
CONTAGEM REGRESSIVA INICIADA...
''')
for c in range(10, 0, -1):
	print(c)
	sleep(1)
print(emoji.emojize(":exclamation:"))