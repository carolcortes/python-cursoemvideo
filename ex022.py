nome = str(input('Digite seu nome completo: ')).strip()
print(f'Analisando seu nome...\n'
      f'Seu nome em maiúsculas é {nome.upper()}nome = str(input('Digite seu nome completo: ')).strip()
print(f'Analisando seu nome...\n'
      f'Seu nome em maiúsculas é {nome.upper()}\n'
      f'Seu nome em minúsculas é {nome.lower()}\n'
      f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras.\n'
      f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras.')
