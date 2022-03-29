print('\033[1;97;43m=' * 8, 'LOJAS CATACOISA E CIA LTDA', '=' * 8, '\033[m')
preco = float(input('Informe o preço das compras: R$ '))
condicao = int(input('Qual a forma de pagamento?\n'
                     '[ 1 ] À vista (dinheiro/cheque)\n'
                     '[ 2 ] À vista no cartão\n'
                     '[ 3 ] Em até 2x no cartão\n'
                     '[ 4 ] Em 3x ou mais no cartão\n'
                print('\033[1;97;43m=' * 8, 'LOJAS CATACOISA E CIA LTDA', '=' * 8, '\033[m')
preco = float(input('Informe o preço das compras: R$ '))
condicao = int(input('Qual a forma de pagamento?\n'
                     '[ 1 ] À vista (dinheiro/cheque)\n'
                     '[ 2 ] À vista no cartão\n'
                     '[ 3 ] Em até 2x no cartão\n'
                     '[ 4 ] Em 3x ou mais no cartão\n'
                     'Informe a condição de pagamento: '))
if condicao <= 4:
    print('O valor total a ser pago', end='')
    if condicao == 1:
        print(f', com 10% de desconto, é de R${preco - (preco * 0.1):.2f}.')
    elif condicao == 2:
        print(f', com 5% de desconto, é de R${preco - (preco * 0.05):.2f}.')
    elif condicao == 3:
        print(f' é de R${preco:.2f}.\n'
              f'Valor das parcelas: 2 x R${preco / 2:.2f}.')
    else:
        print(f', com 20% de juros, é de R${preco * 1.2:.2f}.')
        np = int(input('Informe o número de parcelas: '))
        if np >= 3:
            print(f'Valor das parcelas: {np} x R${(preco * 1.2) / np:.2f}.')
else:
    print('Condição de pagamento inválida. Tente novamente.')
