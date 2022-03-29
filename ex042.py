print('\033[1;34m-=' * 12)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 12, '\033[m')
r1 = float(input('Informe o primeiro segmento: '))
r2 = float(input('Informe o segundo segmento: '))
r3 = float(input('Informe o terceiro segmento: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
      print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
      if r1 == r2 == r3:
            print('EQUILÁTERO.')
      elif r1 != r2 != r3 != r1:
            print('ESCALENprint('\033[1;34m-=' * 12)
print('ANALISADOR DE TRIÂNGULOS')
print('-=' * 12, '\033[m')
r1 = float(input('Informe o primeiro segmento: '))
r2 = float(input('Informe o segundo segmento: '))
r3 = float(input('Informe o terceiro segmento: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
      print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
      if r1 == r2 == r3:
            print('EQUILÁTERO.')
      elif r1 != r2 != r3 != r1:
            print('ESCALENO.')
      else:
            print('ISÓSCELES.')
else:
      print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')
