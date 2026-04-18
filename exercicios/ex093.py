# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
# aula19

jogador = {'nome': str(input('Nome do Jogador: ')), 'gols': []}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for x in range(0, partidas):
    jogador['gols'].append(int(input(f'    Quantos gols na partida {x + 1}? ')))
jogador['total'] = sum(jogador['gols'])
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')    # Também podemos fazer {len(jogador["gols"])} no lugar de {partidas}
for x in range(0, partidas):
    print(f'    => Na partida {x + 1}, fez {jogador["gols"][x]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
