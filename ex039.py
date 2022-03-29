from datetime import date
ano = date.today().year
anonasc = int(input('Informe o ano do seu nascimento: '))
genero = int(input('Informe seu gênero:\n'
                   '[ 1 ] Masculino\n'
                   '[ 2 ] Feminino\n'
                   'Selecione a opçãfrom datetime import date
ano = date.today().year
anonasc = int(input('Informe o ano do seu nascimento: '))
genero = int(input('Informe seu gênero:\n'
                   '[ 1 ] Masculino\n'
                   '[ 2 ] Feminino\n'
                   'Selecione a opção: '))
if genero == 2:
    print('O alistamento não é obrigatório.')
elif genero == 1:
    if ano - anonasc == 18:
        print('Você já tem 18 anos!\n'
          'Você tem que se alistar IMEDIATAMENTE!')
    elif ano - anonasc < 18:
        print(f'Você tem {ano - anonasc} anos.\n'
          f'Ainda faltam {18 - (ano - anonasc)} anos para seu alistamento.\n'
          f'Seu alistamento será em {anonasc + 18}.')
    else:
        print(f'Você tem {ano - anonasc} anos.\n'
          f'Você já deveria ter se alistado há {(ano - anonasc) - 18} anos.\n'
          f'Seu alistamento foi em {anonasc + 18}.')
else:
    print('Opção de gênero inválida. Tente novamente.')