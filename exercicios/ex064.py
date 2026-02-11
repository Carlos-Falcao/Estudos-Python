# Crie um programa que leia varios números inteiros pelo teclado. O programa ira parar quando o usuario digitar o valor 999.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# aula14

# Meu método:
"""
n = xNum = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        xNum += 1
print(f'Você digitou {xNum} números e a soma entre eles foi {soma}.')
"""

# Método Guanabara:
# Como estamos recebendo o flag do lado de fora tbm, ao receber 999 ele não execulta o while.
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
