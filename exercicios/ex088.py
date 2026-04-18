# Crie um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
# aula18

from random import randint
from time import sleep

jogos = []
nums = []
numJogos = 0

print('--'*30)
print(f'{'JOGO NA MEGA SENA':^60}')
print('--'*30)
numJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{'-='*10} SORTEANDO {numJogos} JOGOS {'-='*10}')
for j in range(0, numJogos):
    for x in range(0, 6):
        n = randint(1, 60)
        if n in nums:
            n = randint(1, 60)
        nums.append(n)
        nums.sort()
    jogos.append(nums[:])
    nums.clear()
for j in range(0, numJogos):
    print(f'Jogo {j + 1}: {jogos[j]}')
    sleep(1)
print(f'{'-='*10} < BOA SORTE! > {'-='*10}')
