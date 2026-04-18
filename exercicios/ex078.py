# Crie um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
# aula17

valores = []
maior = menor = 0
posMaior = []
posMenor = []
for x in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {x}: ')))  
    if x == 0:
        maior = menor = valores[x]
        posMaior.append(0)
        posMenor.append(0)
    else:
        if valores[x] >= maior:
            if valores[x] > maior:
                posMaior = []
            maior = valores[x]
            posMaior.append(x)
        if valores[x] <= menor:
            if valores[x] < menor:
                posMenor = []
            menor = valores[x]
            posMenor.append(x)
print('-=' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for x in range(0, len(posMaior)):
    print(f'{posMaior[x]}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições', end=' ')
for x in range(0, len(posMenor)):
    print(f'{posMenor[x]}...', end=' ')

# Diferenças do método Guanabara:

## Ele não criou listas para a Posição do maior/menor
"""
for x in range(0, 5):
    valores.append(int(input('Digite um valor para a Posição {x}: ')))
    if x == 0:
        maior = menor = valores[x]
    else:
        if valores[x] > maior:
            maior = valores[x]
        if valores[x] < menor:
            menor = valores[x]
"""
# Apos o for de verificação para o maior e menor, ele fez outro for para verificar as posições.
"""
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for c, x in enumerate(valores):
    if x == maior:
        print(f'{c}...', end=' ')
"""
# E usou o mesmo método para o menor.
