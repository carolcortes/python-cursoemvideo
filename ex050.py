s = 0
p = 0
for c in range (0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
        p += 1
if p == 1:
    print(s = 0
p = 0
for c in range (0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
        p += 1
if p == 1:
    print('Você informou apenas 1 número par e ', end='')
elif p > 1:
    print(f'Você informou {p} números pares e ', end='')
else:
    print('Você não informou números pares, então ', end='')
print(f'a soma destes valores é {s}.')
