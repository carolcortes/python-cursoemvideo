cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'boldsub':'\033[1;4m'}
v = float(input('Velocidade do carro: '))
if v > 80:
    print(f'Velocidade acima do limite permitido, que é de {cores["boldsub"]}80km/h{cores["limpa"]}.\n'
      f'Você foi multado em {cores["vermelho"]}R${(v - 80) * 7:.2f}{cores["limpa"]}.')
print('Tenha um bom dia! Dirija com segurança.')               cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'boldsub':'\033[1;4m'}
v = float(input('Velocidade do carro: '))
if v > 80:
    print(f'Velocidade acima do limite permitido, que é de {cores["boldsub"]}80km/h{cores["limpa"]}.\n'
      f'Você foi multado em {cores["vermelho"]}R${(v - 80) * 7:.2f}{cores["limpa"]}.')
print('Tenha um bom dia! Dirija com segurança.')