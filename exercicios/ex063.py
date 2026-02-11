# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de Fibonacci.
# Ex: 0, 1, 1, 2, 3, 5, 8.
# aula14

print('---' * 20)
print('Sequencia de Fibonacci')
print('---' * 20)

termos = int(input('Quantos termos você quer mostrar? '))
quantia = 3
a, b = 0, 1
res = a + b

print('~~~' * 20)
print(f'{a} -> {b} -> ', end='')
while quantia <= termos:
    print(f'{res} -> ', end='')
    a = b
    b = res
    res = a + b
    quantia += 1
print('FIM')
print('~~~' * 20)
