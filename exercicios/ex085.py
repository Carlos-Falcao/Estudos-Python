# Crie um programa onde que o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente.
# aula18

valores = [[], []]
for x in range(0, 7):
    num = int(input(f'Digite o {x+1}o valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(valores[0])}')
print(f'Os valores impares digitados foram: {sorted(valores[1])}')
