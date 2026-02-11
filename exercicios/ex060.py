# Crie um programa que leia um número e mostre o seu fatorial
# Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
# aula14

# Método sem biblioteca:
n = int(input('Digite um número para calcular seu fatorial: '))
fat = 1
print(f'Calculando {n}! = ', end='')
while n > 0:
    fat *= n
    if n == 1:
        print(f'{n} = {fat}')
    else:
        print(f'{n} X ', end='')
    n -= 1

# Usando biblioteca (OBS: para saber da existencia dessa biblioteca):
"""
from math import factorial

n = int(input('Digite um número para calcular seu fatorial: '))
res = factorial(n)
print(f'{n}! = {res}')
"""

# Método Guanabara:
"""
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
"""
