e = str(input('Digite a expressão para análise: ')).strip()
pilha = []
for simbolo in e:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()  # A cada parênteses fechado, um aberto é removido.
        else:
            pilha.append(')')  # Se não tiver parênteses aberto, o fechado mantém na pilha.
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
                                 e = str(input('Digite a expressão para análise: ')).strip()
pilha = []
for simbolo in e:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()  # A cada parênteses fechado, um aberto é removido.
        else:
            pilha.append(')')  # Se não tiver parênteses aberto, o fechado mantém na pilha.
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')
