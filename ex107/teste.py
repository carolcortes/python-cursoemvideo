from ex107 import moeda
p = float(input('Digite o preço: R$ '))
print(f' - A metade do preço de {p} é {moeda.metade(p)}.\n'
      f' - O dobro do preço é {moeda.dobrfrom ex107 import moeda
p = float(input('Digite o preço: R$ '))
print(f' - A metade do preço de {p} é {moeda.metade(p)}.\n'
      f' - O dobro do preço é {moeda.dobro(p)}.\n'
      f' - Aumentando 10%, temos {moeda.aumentar(p, 10)}.\n'
      f' - Reduzindo 13% temos {moeda.diminuir(p, 13)}.')
