from random import randint
from time import sleep
numero = randint(0, 5)
print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar! ')
print('-=-' * 18)
adivinha = int(input('Em qual número pefrom random import randint
from time import sleep
numero = randint(0, 5)
print('-=-' * 18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar! ')
print('-=-' * 18)
adivinha = int(input('Em qual número pensei? '))
print('PROCESSANDO...')
sleep(2)
print(f'Você acertou! O número escolhido foi {numero}!' if adivinha == numero
      else f'Você errou! O número escolhido foi {numero}.')
