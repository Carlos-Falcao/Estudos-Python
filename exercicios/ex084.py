# Crie um programa que leia o nome e peso de varias pessoas, guardando tudo em uma lista. No final mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas,
# C) Uma listagem com as pessoas mais leves.
# aula18

# Método Guanabara:
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Idade: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')

# Meu método:
"""
pessoa = []
pesados = []
leves = []
totpessoas = pesoMaior = pesoMenor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if totpessoas == 0:
        pesoMaior = pesoMenor = pessoa[1]
        pesados.append(pessoa[0])
        leves.append(pessoa[0])
    else:
        if pessoa[1] >= pesoMaior:
            if pessoa[1] > pesoMaior:
                pesados.clear()
            pesoMaior = pessoa[1]
            pesados.append(pessoa[0])
        if pessoa[1] <= pesoMenor:
            if pessoa[1] < pesoMenor:
                leves.clear()
            pesoMenor = pessoa[1]
            leves.append(pessoa[0])
    totpessoas += 1
    pessoa.clear()
    stay = ' '
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while stay not in 'SN':
        stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'N':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {totpessoas} pessoas.')
print(f'O maior peso foi de {pesoMaior:.1f}Kg. Peso de {pesados}')
print(f'O menor peso foi de {pesoMenor:.1f}Kg. Peso de {leves}')
"""