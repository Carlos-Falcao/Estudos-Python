# Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
# aula19

# Outro método:
jogadores = list()
jogador = dict()
gols = list()
partidas = 0
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for x in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na partida {x + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    while True:
        conti = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if conti in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if conti == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--'*20)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end=' ')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()
print('--'*20)
while True:
    opcao = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opcao == 999:
        break
    elif opcao > len(jogadores):
        print(f'ERRO! Não existe jogador com código {opcao}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opcao]["nome"]}:')
        for i, gol in enumerate(jogadores[opcao]['gols']):
            print(f'    No jogo {i+1} fez {gol} gols.')
print('--'*20)
print('<< VOLTE SEMPRE >>')


# Primeiro código:
"""
jogadores = list()
jogador = dict()
gols = list()
partidas = cod = 0
while True:
    jogador.clear()
    gols.clear()
    jogador['cod'] = cod
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for x in range(0, partidas):
        gols.append(int(input(f'    Quantos gols na partida {x + 1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    conti = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while conti not in 'SN':
        print('ERRO! Digite S ou N.')
        conti = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if conti == 'N':
        break
    cod += 1
print('-='*30)
print(f'{'cod':<5} {'nome':<12} {'gols':<12} {'total':>10}')
print('--'*20)
for j in jogadores:
    print(f'{j["cod"]:<5} {j["nome"]:<12} {j["gols"]} {j["total"]:>10}')
print('--'*20)
while True:
    opcao = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    while opcao > len(jogadores) - 1 and opcao != 999:
        print(f'ERRO! Não existe jogador com código {opcao}!')
        print('--'*20)
        opcao = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opcao == 999:
        break
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opcao]["nome"]}:')
    for j in jogadores:
        if j['cod'] == jogadores[opcao]['cod']:
            for index, gol in enumerate(j['gols']):
                print(f'    No jogo {index} fez {gol} gols.')
print('<< VOLTE SEMPRE >>')
"""