# Crie um programa que vai ler vários números e colocalos em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os impares digitados, respectivamente. Ao final, mostre o conteudo das 3 listas geradas.
# aula17

listaTotal = []
listaPares = []
listaImpares = []
while True:
    n = int(input('Digite um número: '))
    listaTotal.append(n)
    if n % 2 == 0:
        listaPares.append(n)
    else:
        listaImpares.append(n)
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while stay not in 'SN':
        stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'N':
        break
print('-=' * 30)
print(f'A lista completa é {listaTotal}')
print(f'A lista de pares é {listaPares}')
print(f'A lista de impares é {listaImpares}')
