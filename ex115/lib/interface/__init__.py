def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro! Digite uma opção válida.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return '<não informado>'
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha(), f'\n {txt.upper():^42} \n' + linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[1;32mInforme a opção: \033[m')
    return opc
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro! Digite uma opção válida.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return '<não informado>'
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha(), f'\n {txt.upper():^42} \n' + linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[1;32mInforme a opção: \033[m')
    return opc
