x = '\033[1;4m=\033[m' * 30
print(f'{x}\n    SEQUÊNCIA DE FIBONACCI\n{x}\n')
t = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
print(n1, ' ⇾', n2, end='')
cont = 3
while cont <= t:
    f = n1 + n2
    print(' ⇾', f, end='')
    n1 = n2
    n2 = f
    cont += 1
print(' ⇾ FIM')

                                                                                                                                                                                                                          x = '\033[1;4m=\033[m' * 30
print(f'{x}\n    SEQUÊNCIA DE FIBONACCI\n{x}\n')
t = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
print(n1, ' ⇾', n2, end='')
cont = 3
while cont <= t:
    f = n1 + n2
    print(' ⇾', f, end='')
    n1 = n2
    n2 = f
    cont += 1
print(' ⇾ FIM')

