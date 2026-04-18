# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
# aula19

# Método do Guanabara:
from random import randint
from time import sleep
from operator import itemgetter   # Biblioteca para mais funções e usos em operações matemáticas. Itemgetter serve para indicar qual indice o computador tem que observar.

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # sorted: Gera uma nova lista organizada. key=itemgetter(1): Indica qual index vai observar. 
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for index, valor in enumerate(ranking):
    print(f'    {index + 1}° lugar: {valor[0]} com {valor[1]}.')
    sleep(1)

# Meu método:
"""
from random import randint
from time import sleep

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
pessoa = str()
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*30)
print('== RANKING DOS JOGADORES ==')
for pos in range(0, 4):
    maior = 0
    for k, v in jogadores.items():
        if maior < v:
            maior = v
            pessoa = k
    print(f'{pos + 1}° lugar: {pessoa} com {maior}.')
    sleep(1)
    del jogadores[pessoa]
"""
