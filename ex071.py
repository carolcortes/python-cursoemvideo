x = '\033[1;4m¨\033[m' * 21
print(f'{x}\n  BANCO JOAQUINHO\n{x}')
saque = int(input('Informe o valor do saque: R$ '))
while saque != 0:
    print('{:^20}'.format('\n\033[1;4mTOTAL DE CÉDULAS:\033[m'))
    if saque // 50 > 0:
        print(f'{(saque//50)} cédulas de R$50.00')
        saque -= (saque//50) * 50
    if saque // 20 > 0:
        print(f'{saque//20} cédulas de R$20.00')
        saque -= (saque//20) * 20
    if (saque // 10) > 0:
        print(f'{saque//10} cédulas de R$10.00')
        saque -= (saque//10) * 10
    else:
        print(f'{saque} cédulas de R$1.00')
        saque -= saque
print('\nOperação finalizada.\nVolte sempre ao Banco Joaquinho!')
                                                                                   x = '\033[1;4m¨\033[m' * 21
print(f'{x}\n  BANCO JOAQUINHO\n{x}')
saque = int(input('Informe o valor do saque: R$ '))
while saque != 0:
    print('{:^20}'.format('\n\033[1;4mTOTAL DE CÉDULAS:\033[m'))
    if saque // 50 > 0:
        print(f'{(saque//50)} cédulas de R$50.00')
        saque -= (saque//50) * 50
    if saque // 20 > 0:
        print(f'{saque//20} cédulas de R$20.00')
        saque -= (saque//20) * 20
    if (saque // 10) > 0:
        print(f'{saque//10} cédulas de R$10.00')
        saque -= (saque//10) * 10
    else:
        print(f'{saque} cédulas de R$1.00')
        saque -= saque
print('\nOperação finalizada.\nVolte sempre ao Banco Joaquinho!')
