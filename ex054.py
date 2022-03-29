from datetime import date
ano = date.today().year
maior = []
menor = []
for c in range(1, 8):
    p = int(input(f'Informe o ano de nascimento da {c}º pessoa: '))
    if p <= 2001:
        maior.append(p)
    else:
        menor.append(p)
if len(maior) != 0 and len(menor) != 0:
    print(f'Ao total, {len(maior)}', end='')
    if len(maior) > 1:
        print(' pessoas são maiores de idade e ', end='')
    else:
        print(' pessoa é maior de idadefrom datetime import date
ano = date.today().year
maior = []
menor = []
for c in range(1, 8):
    p = int(input(f'Informe o ano de nascimento da {c}º pessoa: '))
    if p <= 2001:
        maior.append(p)
    else:
        menor.append(p)
if len(maior) != 0 and len(menor) != 0:
    print(f'Ao total, {len(maior)}', end='')
    if len(maior) > 1:
        print(' pessoas são maiores de idade e ', end='')
    else:
        print(' pessoa é maior de idade e ', end='')
    print(f'{len(menor)}', end='')
    if len(menor) > 1:
        print(' são menores de idade.')
    else:
        print(' é menor de idade.')
elif len(maior) > 0 and len(menor) == 0:
    print('Todas as pessoas informadas são maiores de idade.')
elif len(menor) > 0 and len(maior) == 0:
    print('Todas as pessoas informadas são menores de idade.')
else:
    print('Nenhuma pessoa informada é maior de idade.')
