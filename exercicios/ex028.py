# Escreva um programaque faça o computador pensar um valor entre 0 e 5 e peça para o usuario tentar adivinhar.
# O programa devera escrever na tela se o usuario venceu ou perdeu.
# aula10

from random import randint
from time import sleep

print('\033[1;31m=-\033[m' * 30)
print('\033[4;32mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[1;31m=-\033[m' * 30, '\n')

ale = randint(0, 5)
n = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(3)    # Timer de 3 sec para suspense.

if n == ale:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {ale} e não no {n}!')
