# Crie um programa que leia um número inteiro e diga se ele é ou não um número primo.
# aula 13

n = int(input('Digite um número: '))
cont = 0

for i in range(1, n + 1):
    if n % i == 0:
        print(f'\033[32m{i}', end=' ')
        cont += 1
    else:
        print(f'\033[31m{i}', end=' ')
print(f'\n\033[mO número {n} foi divisivel {cont} vezes.')

if cont == 2:
    print(f'{n} é PRIMO!')
else:
    print(f'{n} Não é PRIMO!')
