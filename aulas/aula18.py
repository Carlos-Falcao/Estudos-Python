# Variáveis Compostas (Listas) Parte 2
# ex084 a ex089

dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[1])

pessoas = list()
pessoas.append(dados[:])    # Agora, tenho uma lista dentro de outra lista

# Outra maneira de criar essa estrutura.
pessoas.clear()

pessoas = [['Pedro',25], ['Maria',19], ['Joao',32]]
print(pessoas[0][0])
print(pessoas[2][1])
print(pessoas[1])

# Pratica:

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

print('-=' * 30)
# Exemplo com for.
galera.clear()

galera = [['Joao', 19], ['Ana', 24], ['Carlos', 18], ['Maria', 42]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

print('-=' * 30)
# Salvar dados.
grupo = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    grupo.append(dado[:])
    dado.clear()

# print(grupo)
# Ou para mostrar apenas o de maior idade
totmai = totmen = 0
for p in grupo:
    if p[1] >= 18:
        print(f'{p[0]} e maior de idade.')
        totmai += 1
    else: 
        print(f'{p[0]} e menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')
