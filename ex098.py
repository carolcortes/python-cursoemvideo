from time import sleep
print(f' \033[1;4m{"CONTADOR":^12}\033[m')


def contador(i, f, p):
    c = i
    if p == 0:
        p = 1
    print(F'CONTAGEM DE {i}from time import sleep
print(f' \033[1;4m{"CONTADOR":^12}\033[m')


def contador(i, f, p):
    c = i
    if p == 0:
        p = 1
    print(F'CONTAGEM DE {i} A {f}, de {abs(p)} em {abs(p)}:')
    print('  →', end=' ')
    if i < f:
        while c <= f:
            print(c, end=' ')
            sleep(0.4)
            c += abs(p)
        print()
    if i > f:
        while c >= f:
            print(c, end=' ')
            sleep(0.4)
            c -= abs(p)
        print()


print('a) ', end='')
contador(1, 10, 1)
print('b) ', end='')
contador(10, 0, 2)
print('c) PERSONALIZE SUA CONTAGEM!')
inicio = int(input('Digite o primeiro termo: '))
fim = int(input('Digite o último termo: '))
passo = int(input('Digite o intervalo entre os termos: '))
contador(inicio, fim, passo)
