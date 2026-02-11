# Melhore o jogo do ex028 onde o computador vai "pensar" em um valor entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer.
# aula14

# Meu método:

from random import randint
from time import sleep

print('\033[1;31m=-\033[m' * 30)
print('\033[4;32mSou seu computador...')
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('Você consegue adivinhar qual foi?\033[m')
print('\033[1;31m=-\033[m' * 30, '\n')

res = randint(0, 10)
n = int(input('Qual o seu palpite? '))
tentativas = 1

print('PROCESSANDO...')
sleep(1)
while n != res:
    if n < res:
        print('Mais... Tente mais uma vez.')
    if n > res:
        print('Menos... Tente mais uma vez.')
    tentativas += 1
    n = int(input('Qual o seu palpite? '))
    print('PROCESSANDO...')
    sleep(1)
print(f'\033[1;32mAcertou com {tentativas} tentativas, Parabens!\033[m')

# Método Guanabara:

"""
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    tentativas += 1
    if jogador == res:
        acertou = True
    else:
        if jogador < res:
            print('Mais... Tente mais uma vez.')
        elif jogador > res:
            print('Menos... Tente mais uma vez.')
print(f'\033[1;32mAcertou com {tentativas} tentativas, Parabens!\033[m')
"""
