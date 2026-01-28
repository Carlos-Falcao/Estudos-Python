# Faça um Programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
# aula09

nome = str(input('Qual o seu nome completo? ')).strip()

print(f'Seu nome tem Silva? \033[31m{'SILVA' in nome.upper()}\033[m')
