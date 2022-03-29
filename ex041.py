from datetime import date
ano = date.today().year
anonasc = int(input('Informe o seu ano de nascimento: '))
i = ano - anonasc
print(f'Você tem {i} anos.')
if i <= 9:
    print('Classificação: \033[1;4mMIRIM\033[m.')
elif i <= 14:
    print('Classificação: \033[1;4mINFANTIL\033[m.')
elif i <= 19:
    print('Cfrom datetime import date
ano = date.today().year
anonasc = int(input('Informe o seu ano de nascimento: '))
i = ano - anonasc
print(f'Você tem {i} anos.')
if i <= 9:
    print('Classificação: \033[1;4mMIRIM\033[m.')
elif i <= 14:
    print('Classificação: \033[1;4mINFANTIL\033[m.')
elif i <= 19:
    print('Classificação: \033[1;4mJUNIOR\033[m.')
elif i <= 25:
    print('Classificação: \033[1;4mSÊNIOR\033[m.')
else:
    print('Classificação: \033[1;4mMASTER\033[m.')
