x = '\033[1;4m-\033[m' * 34
pa = int(input('Informe o primeiro termo da P.A: '))
r = int(input('Informe a razão da P.A: '))
t = int(input('Quantos termos você gostaria de verificar? '))
n1 = pa
cont = 1
total = 0
mais = t
while mais != 0:
    total += mx = '\033[1;4m-\033[m' * 34
pa = int(input('Informe o primeiro termo da P.A: '))
r = int(input('Informe a razão da P.A: '))
t = int(input('Quantos termos você gostaria de verificar? '))
n1 = pa
cont = 1
total = 0
mais = t
while mais != 0:
    total += mais
    while cont <= total:
        print(n1, '⇾ ', end='')
        n1 += r
        cont += 1
    print('...')
    mais = int(input('Quantos termos a mais você gostaria de verificar? '))
print(f'\n  ▶   Progressão finalizada com {total} termos mostrados.')
