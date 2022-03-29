x = '\033[1;4m-+-\033[m' * 8
print(f'{x}\n   ANÁLISE DE VALORES\n{x}\n')
c = 0
v = []
while c < 2:
    n = int(input('Digite um valor: '))
    c += 1
    v.append(n)
mais = str(input('Gostaria de adicionar mais valores? [ S / N ]: ')).strip().upper()[0]
while mais in 'SIM':
        n = int(input('Digite um valor: '))
        v.append(n)
        mais = str(input('Gostaria de adicionar mais valores? [ S / N ]: ')).stx = '\033[1;4m-+-\033[m' * 8
print(f'{x}\n   ANÁLISE DE VALORES\n{x}\n')
c = 0
v = []
while c < 2:
    n = int(input('Digite um valor: '))
    c += 1
    v.append(n)
mais = str(input('Gostaria de adicionar mais valores? [ S / N ]: ')).strip().upper()[0]
while mais in 'SIM':
        n = int(input('Digite um valor: '))
        v.append(n)
        mais = str(input('Gostaria de adicionar mais valores? [ S / N ]: ')).strip().upper()[0]
print(f'\n ▶   Você digitou {len(v)} números e a média entre eles é de {sum(v)/len(v)}.\n'
      f' ▶   {max(v)} foi o maior valor digitado e {min(v)} foi o menor.')
