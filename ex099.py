def maior(* num):
    t = len(num)
    print(f'Analisando os valores informados...\n → ', end='')
    if t > 0:
        for valor in num:
            print(f'{valor}', end=' ')
        print(f'\n → Foram informados {t} números.\n '
              f'→ O maior valor informado foi {max(num)}.\n')
    else:
        print(f'\n → Foram informados 0 números.\n '
              f'→ O maior valor informado foi 0.\n')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
                                                                                                                                                                                                                                                                                                               def maior(* num):
    t = len(num)
    print(f'Analisando os valores informados...\n → ', end='')
    if t > 0:
        for valor in num:
            print(f'{valor}', end=' ')
        print(f'\n → Foram informados {t} números.\n '
              f'→ O maior valor informado foi {max(num)}.\n')
    else:
        print(f'\n → Foram informados 0 números.\n '
              f'→ O maior valor informado foi 0.\n')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
