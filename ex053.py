print('\033[1;4m   VERIFICADOR DE PALÍNDROMOS   \033[m')
p = str(input('Digite uma frase ou palavra: ')).strip().upper()
p2 = p.replace(' ', '')
v = p2[::-1]
if ' ' in p:
    print(f'A frase \"{p2}\"', end='')
else:print(f'A palavra \"{p2}\"', end='')
print(f' ao contrário é \"{v}\".')
if v == p2:
    print('Então, \033[1;4;34mÉ PALÍNDROMO\033[m.')
else:
    print('Então, \033[1;4;31mNÃO É PALÍNDROMO\033[m.')
print('\033[1;4m ' * 31, '\033[m')
                                                              print('\033[1;4m   VERIFICADOR DE PALÍNDROMOS   \033[m')
p = str(input('Digite uma frase ou palavra: ')).strip().upper()
p2 = p.replace(' ', '')
v = p2[::-1]
if ' ' in p:
    print(f'A frase \"{p2}\"', end='')
else:print(f'A palavra \"{p2}\"', end='')
print(f' ao contrário é \"{v}\".')
if v == p2:
    print('Então, \033[1;4;34mÉ PALÍNDROMO\033[m.')
else:
    print('Então, \033[1;4;31mNÃO É PALÍNDROMO\033[m.')
print('\033[1;4m ' * 31, '\033[m')
