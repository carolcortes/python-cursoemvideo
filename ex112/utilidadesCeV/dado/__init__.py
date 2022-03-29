def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.idef leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalnum() or entrada == '':
            print(f'\033[1;31mERRO! \"{entrada}\" é um preço inválido.\033[m')
        else:
            valido = True
            return float(entrada)
