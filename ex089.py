x = '-~' * 15
print(f'{x}\n    \033[1;4mEEEM DOM BISCOITINHO\033[m\n{x}\n'
      'Disciplina: Técnicas de Caça\nProfª: Bolacha')
print('-' * 30)
notas = []
dados = []
cont = 1
while True:
    print(f'CÓDIGO DO ALUNO: {cont:2}')
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('1ª nota: ')))
    dados.append(float(x = '-~' * 15
print(f'{x}\n    \033[1;4mEEEM DOM BISCOITINHO\033[m\n{x}\n'
      'Disciplina: Técnicas de Caça\nProfª: Bolacha')
print('-' * 30)
notas = []
dados = []
cont = 1
while True:
    print(f'CÓDIGO DO ALUNO: {cont:2}')
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('1ª nota: ')))
    dados.append(float(input('2ª nota: ')))
    dados.append((dados[1] + dados[2])/2)
    notas.append(dados[:])
    dados.clear()
    print('-' * 30)
    cont += 1
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Deseja adicionar mais um aluno? ')).strip().upper()[0]
    if mais == 'N':
        break
print('{:^5}'.format('\033[1mCÓD.'), '{:<20}'.format('  NOME'), '{:^10}'.format('MÉDIA\033[m'))
for posicao in range(0, len(notas)):
    print(f'{posicao+1:^4}   {notas[posicao][0]:<16}  {notas[posicao][3]:^10.1f}')
cod = []
print('\nDigite o código do aluno para consultar as notas das provas.\n'
      'Para encerrar o programa, digite \"0\".')
while cod != 0:
    cod = int(input('→ \033[4mCódigo:\033[m '))
    if cod > len(notas)+1:
        print(f' ❌ Opção inválida. Digite o código do aluno ou \"0\" para encerrar o programa.')
    elif cod != 0:
        print(f' • As notas de {notas[cod-1][0]} foram {notas[cod-1][1]} e {notas[cod-1][2]}, respectivamente, '
              'na 1ª e 2ª prova.')
    else:
        print('Consulta encerrada!')
