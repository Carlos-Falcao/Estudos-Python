# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - até 9 anos: MIRIM
# - até 14 anos: INFANTIL
# - até 19 anos: JUNIOR
# - até 25 anos: SENIOR
# - acima: MASTER
# aula12

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
