# Crie um programa que leia o ano de nascimento de uma pessoa e de acordo com sua idade, mostre se ele 'ainda vai se alistar', 'é a hora de se alistar' ou 'passou o tempo'.
# O programa também deverá mostrar o tempo que falta ou que passou do prazo.
# aula12

from datetime import date

ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
anoAlistamento = ano + 18
genero = str(input('Qual o seu Gênero: ')).strip().lower()

print('-=-' * 20)
print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')
if genero == 'masculino':
    if idade == 18:
        print(f'Você tem que se alistar IMEDIATAMENTE!')
    elif idade > 18:
        print(f'Você já deveria ter se alistado há {date.today().year - anoAlistamento} anos')
        print(f'Seu alistamento foi em {anoAlistamento}.')
    else:
        print(f'Ainda faltam {anoAlistamento - date.today().year} anos para o alistamento.')
        print(f'Seu alistamento sera em {anoAlistamento}.')
else:
    print('Você não precisa fazer o alistamento obrigatório.')
print('-=-' * 20)
