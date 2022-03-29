reais = float(input('Quanto dinheiro você tem na carteira? R$'))
print(f'Com R${reais}, você pode comprar US${reais/3.27:.2f}.')

lp = float(input('Largura da parede: '))
ap = float(input('Altura da parede: '))
print(f'Sua parede tem a dimensão de {lp}x{ap} e sua área é de {lp*ap}m².\n'
      f'Para pintar essa parede, você precisará de {(lp*ap)/2}L de tinta.')
