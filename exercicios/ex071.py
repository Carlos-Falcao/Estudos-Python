# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuario qual sera o valor a ser sacado e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere as cédulas de 50, 20, 10 e 1 real.
# aula15

print('==' * 20)
print(f'{'BANCO DO FALCAO':^40}')
print('==' * 20)
saque = int(input('Que valor você quer sacar? R$'))

# Método Guanabara:
total = saque
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break

# Meu método:
"""
valor50 = valor20 = valor10 = valor1 = 0
while saque >= 50:
    saque -= 50
    valor50 += 1
while saque >= 20:
    saque -= 20
    valor20 += 1
while saque >= 10:
    saque -= 10
    valor10 += 1
while saque >= 1:
    saque -= 1
    valor1 += 1
if valor50 >= 1:
    print(f'Total de {valor50} cédulas de R$50')
if valor20 >= 1:
    print(f'Total de {valor20} cédulas de R$20')
if valor10 >= 1:
    print(f'Total de {valor10} cédulas de R$10')
if valor1 >= 1:
    print(f'Total de {valor1} cédulas de R$1')
"""

print('==' * 20)
print('Volte sempre ao BANCO DO FALCAO! Tenha um bom dia!')
