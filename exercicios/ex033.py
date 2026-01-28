# Crie um programa que leia 3 números e mostre na tela qual o MAIOR e qual o MENOR.
# aula10

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

'''
    Metodo usado pelo Guanabara

# Verificar menor número
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# Verificar maior número
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

'''


print(f'O menor valor digitado foi \033[1;31m{min(a, b, c)}\033[m')
print(f'O maior valor digitado foi \033[1;32m{max(a, b, c)}\033[m')
