x = '\033[1;4m-+-\033[m' * 7
print(f'{x}\n   SOMANDO VALORES\n{x}\n'
      f'Digite os valores para obter a soma e o número total de termos.\n'
      f'Para encerrar o programa, digite o valor \033[4m999\033[m.\n')
n = s = c = 0
n = int(input('Digite um valor: '))
while n != 999:
    s += n
    c += 1
    nx = '\033[1;4m-+-\033[m' * 7
print(f'{x}\n   SOMANDO VALORES\n{x}\n'
      f'Digite os valores para obter a soma e o número total de termos.\n'
      f'Para encerrar o programa, digite o valor \033[4m999\033[m.\n')
n = s = c = 0
n = int(input('Digite um valor: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um valor: '))
print(f' ▶   Foram digitados {c} números e a soma entre eles é {s}.')

