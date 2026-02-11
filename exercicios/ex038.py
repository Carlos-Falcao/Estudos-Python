# Escreva um programa que leia dois números inteiros e mostre na tela uma mensagem:
# - O PRIMEIRO valor é maior.
# - O SEGUNDO valor é maior.
# - Não existe valor maior, os dois são IGUAIS.
# aula12

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('O PRIMEIRO valor é maior.')
elif num2 > num1:
    print('O SEGUNDO valor é maior.')
else:
    print('Não existe valor maior, os dois são IGUAIS.')
