from time import sleep
print('\033[1;4mDigite 4 valores abaixo:\033[m')
v = int(input('1º: ')), int(input('2ª: ')), int(input('3º: ')), int(input('4º: '))
print(' ➝ Processando análise...')
sleep(1)
print(f'Você digitou os valores: \033[4m{v}\033[m.')
if v.count(9) > 1:
    print(f' ✶ O número 9 aparece {v.count(9)} vezes.')
elif v.count(9) == 1:
    print(f' ✶ O nfrom time import sleep
print('\033[1;4mDigite 4 valores abaixo:\033[m')
v = int(input('1º: ')), int(input('2ª: ')), int(input('3º: ')), int(input('4º: '))
print(' ➝ Processando análise...')
sleep(1)
print(f'Você digitou os valores: \033[4m{v}\033[m.')
if v.count(9) > 1:
    print(f' ✶ O número 9 aparece {v.count(9)} vezes.')
elif v.count(9) == 1:
    print(f' ✶ O número 9 aparece 1 vez.')
else:
    print(' ✶ O número 9 não está entre os números informados.')
print(f' ✶ O número 3 apareceu na {v.index(3)+1}ª posição.' if 3 in v else ' ✶ O número 3 não está entre os'
                                                                                   ' números informados.')
pares = []
for p in v:
    if p % 2 == 0:
        pares.append(p)
print(f' ✶ Os valores pares digitados foram {pares}.')
