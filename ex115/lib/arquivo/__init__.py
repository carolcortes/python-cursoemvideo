Carol;27
Max;33
Claudia;37
Douglas;21
Bartolo;35
Guigui;13
from ex115.lib.interface import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[7;41mErro ao ler o arquivo!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[7;41mErro ao abrir o arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[7;41mErro ao escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
