# Escreva um programa que leia um número inteiro qualquer e peça para o suario escolher qual sera a base para conversão:
# - 1 para binario
# - 2 para octal
# - 3 para hexadecimal
# aula12

num = int(input('Digite um número inteiro: '))
print('''Escolha uma dessas bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{num} convertido para BINARIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para OCTAL é igual a {hex(num)[2:]}')
else:
    print('\033[1;31mA opção escolhida não existe!\033[m')
