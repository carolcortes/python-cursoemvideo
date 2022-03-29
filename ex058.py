from random import randint
up = '-=-' * 18
print(f'{up}\n Vou pensar em um número de 0 a 10. Tente adivinhar!\n{up}')
n = randint(0, 10)
guess = int(input('Em qual número pensei? '))
c = 1
while guess != n:
    if guess < n:
        guess = int(input('É maior. Tente novamente.\nEm qual número pensei? '))
        c += 1
    else:
        guess = int(input('É menfrom random import randint
up = '-=-' * 18
print(f'{up}\n Vou pensar em um número de 0 a 10. Tente adivinhar!\n{up}')
n = randint(0, 10)
guess = int(input('Em qual número pensei? '))
c = 1
while guess != n:
    if guess < n:
        guess = int(input('É maior. Tente novamente.\nEm qual número pensei? '))
        c += 1
    else:
        guess = int(input('É menor. Tente novamente.\nEm qual número pensei? '))
        c += 1
if c == 1:
    print(f'Você acertou em cheio! O número que pensei foi {n}!')
else:
    print(f'Você acertou com {c} tentativas! O número que pensei foi o {n}.\nParabéns!')
