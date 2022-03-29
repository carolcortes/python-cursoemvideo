def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
            continue
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return '<não informado>'
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mErro! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return '<não informado>'
        else:
            return n


i = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}.')
