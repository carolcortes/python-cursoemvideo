from ex108 import moeda
p = float(input('Digite o preço: R$ '))
print(f' - A metade do preço de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.\n'
      f' - O dobro é {moeda.moeda(moeda.dobro(p))}.\n'
      f' - Aumentando 10%, temos {moeda.mfrom ex108 import moeda
p = float(input('Digite o preço: R$ '))
print(f' - A metade do preço de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.\n'
      f' - O dobro é {moeda.moeda(moeda.dobro(p))}.\n'
      f' - Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}.\n'
      f' - Reduzindo 13% temos {moeda.moeda(moeda.diminuir(p, 13))}.')
