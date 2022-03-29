n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
r = 0
x = '=' * 38
while r != 5:
    r = int(input(f'\033[1;4m{x}\033[m\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Qual o maior?\n[ 4 ] Novos números\n'
                  f'[ 5 ] Sair do programa\nInforme a opção a ser executada: '))
    if r == 1:
        print(f'\n  ▶   A soma entre {n1} e {n2} é igual a {n1+n2}.\n')
    elif r == 2:
        print(f'\n  ▶   A multiplicação entre {n1} e {n2} é igual a {n1*n2}.\n')
    elif r == 3:
        op3 = [n1, n2]
        if n1 == n2:
            print('Os dois númerosn1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
r = 0
x = '=' * 38
while r != 5:
    r = int(input(f'\033[1;4m{x}\033[m\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Qual o maior?\n[ 4 ] Novos números\n'
                  f'[ 5 ] Sair do programa\nInforme a opção a ser executada: '))
    if r == 1:
        print(f'\n  ▶   A soma entre {n1} e {n2} é igual a {n1+n2}.\n')
    elif r == 2:
        print(f'\n  ▶   A multiplicação entre {n1} e {n2} é igual a {n1*n2}.\n')
    elif r == 3:
        op3 = [n1, n2]
        if n1 == n2:
            print('Os dois números são iguais.')
        else:
            print(f'\n  ▶   O número {max(op3)} é maior do que {min(op3)}.')
    elif r == 4:
        print('\n  ▶   Informe os números novamente.')
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif r == 5:
        print(f'{x}\n         PROGRAMA FINALIZADO\n{x}')
    else:
        print('\n   ▶   Opção inválida. Tente novamente.')
