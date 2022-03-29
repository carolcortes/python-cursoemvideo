idades = []
homens = []
idadehomens = []
mulheres = []
for c in range(1, 5):
    print(f'{c}º PESSOA:')
    n = str(input('Nome: ')).strip().title()
    i = int(input('Idade: '))
    idadeidades = []
homens = []
idadehomens = []
mulheres = []
for c in range(1, 5):
    print(f'{c}º PESSOA:')
    n = str(input('Nome: ')).strip().title()
    i = int(input('Idade: '))
    idades.append(i)
    g = str(input('Gênero - [ M ] Masculino [ F ] Feminino -\nInforme a opção escolhida: ')).upper()
    if g == 'M':
        homens.append(n)
        idadehomens.append(i)
    if g == 'F' and i < 20:
        mulheres.append(n)
print('-' * 20)
print(f'1. A média de idade do grupo é de {(sum(idades)) / 4:.0f} anos.')
if len(homens) == 0:
    print('2. Nenhum homem foi informado.')
else:
    print(f'2. {homens[idadehomens.index(max(idadehomens))]} é o homem mais velho e tem {max(idadehomens)} anos.')
if len(mulheres) == 0:
    print('3. Nenhuma mulher possui menos de 20 anos de idade.')
elif len(mulheres) == 1:
    print('3. Apenas 1 mulher possui menos de 20 anos de idade.')
else:
    print(f'3. No total, {len(mulheres)} mulheres possuem menos de 20 anos de idade.')
