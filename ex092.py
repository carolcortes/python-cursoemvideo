from datetime import date
ano = date.today().year
t = {'nome': str(input('Nome: ')).strip().title()}
anonasc = int(input('Ano de nascimento: '))
t['idade'] = ano - anonasc
t['ctps'] = int(input('Nº Cateira de Trabalho (Caso não tenha, digite \"0\"): '))
if t['ctps'] == 0:
    print('-' * 30, f'\n ♢ \033[1;4mDADOS CADASTRADOS:\033[m')
    print(f'Nome: {t["nome"]}\n'
          f'Idade: {t["idade"]} anos\n'
          f'Nº Carteira de Trabalho: CTPS não registrada.')
else:
    t['anocont'] = int(input('Ano de Contratação: '))
    t['salario'] = float(input('Salário: R$'))
    t['aposenta'] = t[from datetime import date
ano = date.today().year
t = {'nome': str(input('Nome: ')).strip().title()}
anonasc = int(input('Ano de nascimento: '))
t['idade'] = ano - anonasc
t['ctps'] = int(input('Nº Cateira de Trabalho (Caso não tenha, digite \"0\"): '))
if t['ctps'] == 0:
    print('-' * 30, f'\n ♢ \033[1;4mDADOS CADASTRADOS:\033[m')
    print(f'Nome: {t["nome"]}\n'
          f'Idade: {t["idade"]} anos\n'
          f'Nº Carteira de Trabalho: CTPS não registrada.')
else:
    t['anocont'] = int(input('Ano de Contratação: '))
    t['salario'] = float(input('Salário: R$'))
    t['aposenta'] = t['anocont'] + 35 - anonasc
    print('-' * 30, f'\n ♢ \033[1;4mDADOS CADASTRADOS:\033[m')
    print(f'Nome: {t["nome"]}\n'
          f'Idade: {t["idade"]} anos\n'
          f'Nº Carteira de Trabalho: {t["ctps"]} \n'
          f'Salário: R${t["salario"]:.2f}\n'
          f' → Aposentadoria previsa para o ano de {t["anocont"] + 35}, com {t["aposenta"]} anos.')
print('-' * 30)
print(t)
