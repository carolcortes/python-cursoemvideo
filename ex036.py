casa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o valor do seu salário: R$ '))
tempo = int(input('Quantos anos de financiamento? '))
prestacao = casa / (tempo*12)
if prestacao <= salario * 0.3:
    print(f'Seu empréstimo foi aprovado!\n'
          f'Sua prestação mensal será de R${prestacao:.2f}')
else:
    print(f'Empréstimo negado!\n'
          f'A prescasa = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o valor do seu salário: R$ '))
tempo = int(input('Quantos anos de financiamento? '))
prestacao = casa / (tempo*12)
if prestacao <= salario * 0.3:
    print(f'Seu empréstimo foi aprovado!\n'
          f'Sua prestação mensal será de R${prestacao:.2f}')
else:
    print(f'Empréstimo negado!\n'
          f'A prestação mensal de R${prestacao:.2f} excede o valor máximo de 30% de seu salário.')
