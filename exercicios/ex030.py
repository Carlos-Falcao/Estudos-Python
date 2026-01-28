# Crie um programa que leie um número inteiro e mostre na tela se ele é PAR ou IMPAR
# aula10

num = int(input('Digite um número: '))
val = num % 2

if val == 0:
    print(f'O número {num} é \033[35mPAR\033[m')
else:
    print(f'O número {num} é \033[35mIMPAR\033[m')
