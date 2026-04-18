# Crie um tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileirão de Futebol, na ordem de colocação. Depois mostre:
# A) Os 5 primeiros.
# B) Os ultimos 4 colocados.
# C) Times em ordem alfabética.
# D) Em que posição esta o time da Chapecoense.
# aula16

timesBrasil = ('Palmeiras', 'São Paulo', 'Fluminese', 'Bahia', 'Athletico-PR', 'Bragantino',
               'Chapecoense', 'Mirassol', 'Coritiba', 'Flamengo', 'Botafogo', 'Corinthians',
               'Grêmio', 'Vitória', 'Atlético-MG', 'Remo', 'Vasco', 'Santos', 'Internacional', 'Cruzeiro')
print('-=' * 20)
print(f'Lsita de times do Brasileirão: {timesBrasil}')
print('-=' * 20)
print(f'Os 5 primeiros são {timesBrasil[:5]}')
print('-=' * 20)
print(f'Os 4 ultimos são {timesBrasil[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(timesBrasil)}')
print('-=' * 20)
print(f'O Chapecoense esta na {timesBrasil.index("Chapecoense") + 1}ª posição.')
