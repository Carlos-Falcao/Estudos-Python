# Faça um Programa que leia um número real qualquer e mostre sua porção inteira.
# aula08

from math import trunc

num = float(input('Digite um número: '))

print(f'O número {num} tem a parte inteira {trunc(num)}.')
