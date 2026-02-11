# Crie um programa que calcule a soma de todos os números impares que são multiplos de 3 e que se encontram no intervalo de 1 a 500.
# aula13

s = 0
count = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        count += 1
        s += i

print(f'A soma de todos os {count} valores solicitados é {s}')
