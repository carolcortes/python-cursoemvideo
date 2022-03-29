n = int(input('Informe um número: '))
bc = int(input('Qual será a base de conversão?\n'
               '[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal\n'
               'Informe sua resposta: '))
if bc == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif bc == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}.')
elif bc == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}.')
else:
    print('Opção inválida. Tentn = int(input('Informe um número: '))
bc = int(input('Qual será a base de conversão?\n'
               '[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal\n'
               'Informe sua resposta: '))
if bc == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif bc == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}.')
elif bc == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}.')
else:
    print('Opção inválida. Tente novamente.')
