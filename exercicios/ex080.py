# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
# aula17

lista = []
for x in range(0, 5):
    num = int(input('Digite um valor: '))
    lista.append(num)
    for indice, valor in enumerate(lista):
        if num <= valor:
            lista.insert(indice, num)
            lista.pop()
            break
    if num == lista[-1]:
        print('Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posição {lista.index(num)} da lista...')
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
