# Faça um Programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.
# aula09

cid = str(input('Em qual cidade você nasceu? ')).strip()

print(cid[:5].upper() == 'SANTO')
