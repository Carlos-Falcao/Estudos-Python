# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
# aula18

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = somColuna = 0
for l in range(0, 3):   # for para acrescentar valores na matriz.
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):   # for para mostrar a matriz.
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*30)
for l in range(0, 3):   # for para calculos com os valores.
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            somColuna += matriz[l][c]
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {somColuna}.')
print(f'O maior valor da segunda linha é {max(matriz[1])}.')
