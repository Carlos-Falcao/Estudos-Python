# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for impar, desconsidere-o.
# aula13

s = 0
cont = 0
for i in range(1, 11):
    n = int(input(f'Digite o {i} valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'A soma dos {cont} números pares inseridos é {s}')
