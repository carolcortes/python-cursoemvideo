from datetime import date
ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
      ano = date.today().year
print(f'O ano {ano} é BISSEXTO.' if ano % 4 == 0 anfrom datetime import date
ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
      ano = date.today().year
print(f'O ano {ano} é BISSEXTO.' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
      else f'O ano {ano} não é BISSEXTO.')
