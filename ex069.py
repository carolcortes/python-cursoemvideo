x = '\033[1;4m-\033[m' * 23
print(f'{x}\n  CADASTRO DE PESSOAS\n{x}')
idade = []
m = f = 0
while True:
    print('\033[1;4mInsira os dados abaixo:\033[m')
    i = int(input('Idade: '))
    if i >= 18:
        idade.append(i)
    g = ' '
    while g not in 'MF':
        g = str(input('Gênero [M / F]: ')).strip().upper()[0]
    if g == 'M':
        m += 1
    elif g == 'F' and i < 20:
        f += 1
    mais = ' '
    while mais not in 'SN':
        mais = str(input(' ▶   Quer continuar? [S / N] ')).strip().upper()[0]
    if mais == 'N':
        break
print('\n\033[1;4mCADASTRAMENTO ENCERRADO!\033[m')
print(f' • {len(idade)} pessoas tem mais de 18 anos.')
print(f' • Foram cadastrados {m} homens.')
print(f' • {f} mulheres tem menos de 20 anos.')
                                                                                                                                                                                                                                        x = '\033[1;4m-\033[m' * 23
print(f'{x}\n  CADASTRO DE PESSOAS\n{x}')
idade = []
m = f = 0
while True:
    print('\033[1;4mInsira os dados abaixo:\033[m')
    i = int(input('Idade: '))
    if i >= 18:
        idade.append(i)
    g = ' '
    while g not in 'MF':
        g = str(input('Gênero [M / F]: ')).strip().upper()[0]
    if g == 'M':
        m += 1
    elif g == 'F' and i < 20:
        f += 1
    mais = ' '
    while mais not in 'SN':
        mais = str(input(' ▶   Quer continuar? [S / N] ')).strip().upper()[0]
    if mais == 'N':
        break
print('\n\033[1;4mCADASTRAMENTO ENCERRADO!\033[m')
print(f' • {len(idade)} pessoas tem mais de 18 anos.')
print(f' • Foram cadastrados {m} homens.')
print(f' • {f} mulheres tem menos de 20 anos.')
