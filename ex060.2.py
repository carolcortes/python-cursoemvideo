from math import factorial
x = '\033[1;4mx-\033[m' * 16
print(f'{x}\n CALCULADORA DE FATORIAL  \033[1m➜ n!\033[m\n{x}\n')
n = int(input('Informe um número: '))
f = factorial(n)
print(f'{n}! = ', end='')
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
print(f)
   from math import factorial
x = '\033[1;4mx-\033[m' * 16
print(f'{x}\n CALCULADORA DE FATORIAL  \033[1m➜ n!\033[m\n{x}\n')
n = int(input('Informe um número: '))
f = factorial(n)
print(f'{n}! = ', end='')
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
print(f)
