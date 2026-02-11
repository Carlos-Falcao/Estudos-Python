# Crie um programa que leia o peso de 5 pessoas. No final, mostre qual foi maior e o menor peso lidos.
# aula13

maiorPeso = 0
menorPeso = 0

for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}º pessoa: '))
    if pessoa == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

print(f'O maior peso lido foi de {maiorPeso:.1f}Kg')
print(f'O menor peso lido foi de {menorPeso:.1f}Kg')
