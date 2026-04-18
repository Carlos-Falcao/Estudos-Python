# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, moestre:
# A) Quantas pessoas cadastradas.
# B) A média de idade.
# C) Uma lista com mulheres.
# D) Uma lista com idade acima da média.
# aula19

publico = list()
pessoa = dict()
totIdade = mediaIdade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    totIdade += pessoa['idade']
    publico.append(pessoa.copy())
    conti = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while conti not in 'SN':
        print('ERRO! Responda S ou N.')
        conti = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if conti in 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(publico)} pessoas cadastradas.')
mediaIdade = totIdade / len(publico)
print(f'B) A média de idade é de {mediaIdade:.2f} anos.')
print('C) As mulheres cadastradas foram', end=' ')
for p in publico:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in publico:
    if p['idade'] >= mediaIdade:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print(' ')
print('<< ENCERRADO >>')
