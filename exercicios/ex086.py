# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
# aula18

# Método Guanabara:
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()

# Meu método:
"""
matriz = []
for x in range(0, 9):
    if x <= 2:
        matriz.append(int(input(f'Digite um valor para [0, {x}]: ')))
    elif x <= 5:
        matriz.append(int(input(f'Digite um valor para [1, {x - 3}]: ')))
    else:
        matriz.append(int(input(f'Digite um valor para [2, {x - 6}]: ')))
print('-='*30)
for e in range(0, len(matriz)):
    print(f'[{matriz[e]:^5}]', end=' ')
    if e == 2 or e == 5:
        print('\n')
"""