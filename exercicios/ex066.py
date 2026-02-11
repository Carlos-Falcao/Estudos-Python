# Crie um programa que leia varios números inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que é a metodo de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
# aula15

cont = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma dos {cont} valores foi {soma}!')
