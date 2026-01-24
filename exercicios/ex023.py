# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# aula09

n = int(input('Informe um numero: '))

u = n // 1 % 10 
d = n // 10 % 10
c = n // 100 % 10       # Ex com 2345 -> 2345/100 = 23.45 porem e divisão inteira. 23/10 = 2, porem o resto da divisão e '3'
m = n // 1000 % 10

print(f'Analisando o numero {n}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
