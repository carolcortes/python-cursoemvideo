def pyhelp(com):
    from time import sleep
    print(f'Acessando o manual do comando \'{comando}\'...')
    sleep(0.5)
    print('\033[7m')
    help(com)
    print('\033[m')
    sleep(1)
    

comando = ''
while True:
    print(f'\033[1;4;30;43m{"SISTEMA DE AJUDA PyHELP":^25}\033[m\n'
          f' ➔ Para encerrar, digite \033[1;4mFIM\033[m.')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        pyhelp(comando)
print('\033[1;97;41m -x- SISTEMA FINALIZADO -x- \033[m')
                                                                                                                                                                                                                                                                      def pyhelp(com):
    from time import sleep
    print(f'Acessando o manual do comando \'{comando}\'...')
    sleep(0.5)
    print('\033[7m')
    help(com)
    print('\033[m')
    sleep(1)
    

comando = ''
while True:
    print(f'\033[1;4;30;43m{"SISTEMA DE AJUDA PyHELP":^25}\033[m\n'
          f' ➔ Para encerrar, digite \033[1;4mFIM\033[m.')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        pyhelp(comando)
print('\033[1;97;41m -x- SISTEMA FINALIZADO -x- \033[m')
