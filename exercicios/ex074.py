# Crie um programa que vai gerar cinco nums aleatorios e colocar em uma tupla.
# Depois disso, mostre a listagem de nums gerados e indique o menor e o maior valor que estão na tupla.
# aula16

from random import randint

valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
# print(f'Os valores sorteados foram: {valores}')
# Maneira para não ficar a formatação comum.
print('Os valores sorteados foram:', end=' ')
for x in valores:
    print(x, end=' ')
print(f'\nO maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
