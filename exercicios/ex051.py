# Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiro termos dessa progressão.
# aula13

print('-=' * 20)
print('OS 10 PRIMEIROS TERMOS DE UMA PA')
print('-=' * 20)

# Meu método:

"""
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for i in range(1, 11):
    print(f'{a1} -> ', end='')
    a1 += r
print('ACABOU')
"""

# Método do Guanabara: 

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
ult = a1 + (10 - 1) * r

for i in range(a1, ult + r, r):
    print(i, end=' -> ')
print('ACABOU')
