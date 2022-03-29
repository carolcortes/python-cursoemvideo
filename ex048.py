for c in range(2, 50 + 1, 2):
    print(c, end=' ')
print('FIM')
s = 0
v = 0
for c in range(1, 500 + 1):
    if c % 2 != 0 and c % 3 == 0:
        v += 1
        s += c
print(f'A soma de todos os {v} valores solicitados é de {s}.')