print('-' * 30+f'\n{"CADASTRO DE PESSOAS":^30}\n'+'-' * 30)
dados = {}
cadastro = []
idade = []
while True:
    dados['nome'] = (str(input('Nome: ')).strip().title())
    while True:
        dados['genero'] = (str(input('Gênero [M/F]: ')).strip().upper()[0])
        if dados['genero'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = (int(input('Idade: ')))
    cadastro.append(dados.copy())
    idade.append(dados['idade'])
    dprint('-' * 30+f'\n{"CADASTRO DE PESSOAS":^30}\n'+'-' * 30)
dados = {}
cadastro = []
idade = []
while True:
    dados['nome'] = (str(input('Nome: ')).strip().title())
    while True:
        dados['genero'] = (str(input('Gênero [M/F]: ')).strip().upper()[0])
        if dados['genero'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = (int(input('Idade: ')))
    cadastro.append(dados.copy())
    idade.append(dados['idade'])
    dados.clear()
    while True:
        mais = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if mais in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if mais == 'N':
        break
print('-' * 30)
print(f'• Foram cadastradas {len(cadastro)} pessoas.\n'
      f'• A média de idade do grupo cadastrado é de {sum(idade)/len(idade):.2f} anos.\n'
      f'• As mulheres cadastradas foram: ', end='')
for m in cadastro:
    if m['genero'] == 'F':
         print(f'{m["nome"]} ', end='')
print('\nAs pessoas com idade acima da média foram:')
for p in cadastro:
    if p['idade'] > (sum(idade)/len(idade)):
        print(f' → {p["nome"]}, do gênero {p["genero"]}, com {p["idade"]} anos.')
print('\n', dados, '\n', cadastro)
