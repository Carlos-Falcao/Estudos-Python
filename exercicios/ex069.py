# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastradas, o programa devera perguntar se o usuario quer ou não continuar. No final mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens tem cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
# aula15

pessoaDeMaior = numHomens = mulherMais20 = 0
while True:
    sexo = stay = ' '
    print('--' * 20)
    print('CADASTRE UM PESSOA')
    print('--' * 20)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    # Verifica o num de Pessoas de Maior.
    if idade > 18:
        pessoaDeMaior += 1
    # Verifica o num de Homens.
    if sexo == 'M':
        numHomens += 1
    # Verifica o num de Mulheres com 20 anos ou mais.
    if sexo == 'F' and idade < 20:
        mulherMais20 += 1
    print('--' * 20)
    while stay not in 'SN':
        stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'N':
        break
print(f'O total de pessoas com mais de 18 anos: {pessoaDeMaior}')
print(f'Ao todo temos {numHomens} homens cadastrados.')
print(f'E temos {mulherMais20} mulheres com menos de 20 anos.')
