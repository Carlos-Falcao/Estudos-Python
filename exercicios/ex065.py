# Crie um programa que leia varios números inteiros pelo teclado. No final, mostre a media entre todos os valores e qual foi o maior e o menor valores lido.
# O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.
# aula14

xValores = soma = maior = menor = 0
stay = 'S'
while stay != 'N':
    n = int(input('Digite um número: '))
    soma += n
    xValores += 1
    if xValores == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / xValores
print(f'Você digitou {xValores} números e a media foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
