valores = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Valor adicionado ao final da lista.')
    else:
        posicao = 0
        while posicao < len(valores):
            if n <= valores[posicao]:
                valores.insert(posicao, n)
                print(f'Valor {n} adicionado à posição {posicao}.')
                break
            posicao += 1
print('-=' * 20)
prvalores = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Valor adicionado ao final da lista.')
    else:
        posicao = 0
        while posicao < len(valores):
            if n <= valores[posicao]:
                valores.insert(posicao, n)
                print(f'Valor {n} adicionado à posição {posicao}.')
                break
            posicao += 1
print('-=' * 20)
print(f'Os valores digitados em ordem foram {valores}.')
