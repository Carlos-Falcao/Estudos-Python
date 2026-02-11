# Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas. No final do programa, mostre:
# -> A média da idade do grupo.
# -> Qual é o nome do homem mais velho.
# -> Quantas mulheres tem menos de 20 anos.
# aula13

# Método Guanabara:

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
mulherMenos20 = 0

for p in range(1, 5):
    print('-' * 15, f'{p}º PESSOA', '-' * 15)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and maiorIdadeHomem < idade:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        mulherMenos20 += 1
mediaIdade = somaIdade / 4

print(f'A média de idade do grupo é de {mediaIdade:.1f} anos.')
print(f'O homem mais velho tem {maiorIdadeHomem} anos e se chama {nomeVelho}.')
print(f'Ao todo são {mulherMenos20} mulheres com menos de 20 anos.')


# Meu método:
# Sofri e tive que pesquisar mais do que era preciso :(

"""
cadastro = []
Hvelho = 0
Hnome = ''
Mjovens = 0

# Recebe as informacoes e salva na lista de cadastro.
for i in range(1, 5):
    print('-' * 15, f'{i}º PESSOA', '-' * 15)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    pessoa = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo
    }
    cadastro.append(pessoa)

# Salva as idades das pessoas em uma lista 'idades'
idades = [p.get('idade') for p in cadastro]
media = sum(idades) / len(idades)

for i in cadastro:
    if i['sexo'].upper() == 'M':
        if i['idade'] > Hvelho:
            Hvelho = i['idade']
            Hnome = i['nome']

for i in cadastro:
    if i['sexo'].upper() == 'F':
        if i['idade'] < 20:
            Mjovens += 1

print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'O homem mais velho tem {Hvelho} anos e se chama {Hnome}.')
print(f'Ao todo são {Mjovens} mulheres com menos de 20 anos.')
"""
