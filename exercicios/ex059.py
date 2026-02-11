# Crie um programa que leia dois valores e mostre um menu como ao lado na tela:
"""
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
"""
# Seu programa devera realizar a operação solicitada em cada caso.
# aula14

from time import sleep

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
opcao = 0

while opcao != 5:
    sleep(2)
    print("""\033[1;33m[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa\033[m""")
    opcao = int(input('>>>>>> Qual a sua opção? ')) 
    if opcao == 1:
        res = num1 + num2
        print(f'A soma entre {num1} + {num2} é {res}!')
    elif opcao == 2:
        res = num1 * num2
        print(f'O resultado de {num1} X {num2} é {res}!')
    elif opcao == 3:
        if num1 > num2 or num2 > num1:
            maior = max(num1, num2)
            print(f'Entre {num1} e {num2}, o maior é {maior}')
        elif num1 == num2:
            print(f'Não ha valor maior, ambos são iguais!')
    elif opcao == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('\033[1;31mOpção invalida! Tente novamente.\033[m')
    print('-=' * 20)
sleep(2)
print('Fim do programa! Volte sempre')
