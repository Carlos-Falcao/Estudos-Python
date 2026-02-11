# Crie um programa que faça o computador jogar Jokenpo com você.
# aula12

from random import randint
from time import sleep

opcoes = ('Pedra', 'Papel', 'Tesoura')

print('''\033[33mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
jogador = int(input('Qual a sua jogada? '))
pc = randint(0, 2)

if jogador not in (0, 1, 2):
    print('JOGADA INVÁLIDA')
    exit()

print('JO')
sleep(.5)
print('KEN')
sleep(.5)
print('PO!!!')

print('-=' * 20)
print(f'Computador jogou {opcoes[pc]}')
print(f'Jogador jogou {opcoes[jogador]}')
print('-=' * 20)

if jogador == pc:
     print('EMPATE')
elif ((jogador == 0 and pc == 2) or 
      (jogador == 1 and pc == 0) or 
      (jogador == 2 and pc == 1)):
    print('JOGADOR VENCE')
else:
    print('COMPUTADOR VENCE')


# Metodo feito pelo Guanabara

'''
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA')
elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA')  
elif pc == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
'''
