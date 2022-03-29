x = '\033[1;4m*=\033[m' * 13
print(f'{x}\n  CALCULADORA DE TABUADA\n{x}')
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print(f' ▶   \033[1;4mTABUADA DE {n}\033[m')
    for c in range(1, 11):
        print(f'  {n} x {c:2} = {n*c}')
print(f'{x}\n    PROGRAMx = '\033[1;4m*=\033[m' * 13
print(f'{x}\n  CALCULADORA DE TABUADA\n{x}')
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        break
    print(f' ▶   \033[1;4mTABUADA DE {n}\033[m')
    for c in range(1, 11):
        print(f'  {n} x {c:2} = {n*c}')
print(f'{x}\n    PROGRAMA ENCERRADO\n{x}')
