# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantos são de maior idade.
# aula13

# Método Guanabara:

from datetime import date

atual = date.today().year
countNovos = 0
countVelhos = 0

for pessoa in range(1,8):
    nasc = int(input(f'Em que ano nasceu a {pessoa}º pessoa? '))
    idade = atual - nasc
    if idade >= 21:
        countVelhos += 1
    else:
        countNovos += 1
print(f'Ao todo tivemos {countVelhos} pessoas maiores de idade')
print(f'E tivemos {countNovos} pessoas menores de idade') 


# Meu método:

"""
countNovos = 0
countVelhos = 0

ano = int(input('Em que ano nasceu a 1º pessoa? '))
ano2 = int(input('Em que ano nasceu a 2º pessoa? '))
ano3 = int(input('Em que ano nasceu a 3º pessoa? '))
ano4 = int(input('Em que ano nasceu a 4º pessoa? '))
ano5 = int(input('Em que ano nasceu a 5º pessoa? '))
ano6 = int(input('Em que ano nasceu a 6º pessoa? '))
ano7 = int(input('Em que ano nasceu a 7º pessoa? '))

idade = [ano, ano2, ano3, ano4, ano5, ano6, ano7]

for i in range(0, 7):
    if idade[i] > 2008:
        countNovos += 1
    else:
        countVelhos += 1

print(f'Ao todo tivemos {countVelhos} pessoas maiores de idade')
print(f'E tivemos {countNovos} pessoas menores de idade') 
"""
