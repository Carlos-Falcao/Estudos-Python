# Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50.
# aula13

for c in range(2, 51, 2):       # Esse método é melhor, menos linha e menos uso do computador.
    print(c, end=' ')
print('Acabou')

# Ou

for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
print('Acabou')
