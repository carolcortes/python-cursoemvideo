p = float(input('Informe seu peso (kg): '))
a = float(input('Informe sua altura (m): '))
imc = p / (a ** 2)
print(f'Seu IMC é de {imc:.1f}.\n'
      f'Você está ',end='')
if imc < 18.5:
    print('abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('no peso ideal.')
elif 25 <= imc < 30:
    print('em sobrepeso.')
elif 30 <= imc < 40:
    print('em obesidade.')
else:
    print('em obesidade mórbida.')
                                                                                                                                                                                                     p = float(input('Informe seu peso (kg): '))
a = float(input('Informe sua altura (m): '))
imc = p / (a ** 2)
print(f'Seu IMC é de {imc:.1f}.\n'
      f'Você está ',end='')
if imc < 18.5:
    print('abaixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('no peso ideal.')
elif 25 <= imc < 30:
    print('em sobrepeso.')
elif 30 <= imc < 40:
    print('em obesidade.')
else:
    print('em obesidade mórbida.')
