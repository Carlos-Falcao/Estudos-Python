# Crie um programa que jogue PAR ou IMPAR com o computador.
# O jogo so sera interrompido quando o jogador PERDER, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
# aula15

from random import randint

print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 20)

wins = 0
while True:
    num = int(input('Digite um valor: '))
    computador = randint(0, 10)
    tot = num + computador
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print('--' * 20)
    print(f'Você jogou {num} e o computador {computador}. Total de {tot} ', end='')
    print('DEU PAR' if tot % 2 == 0 else 'DEU IMPAR')
    print('--' * 20)
    if tot % 2 == 0:
        if opcao in 'Pp':
            print('Você VENCEU!')
            wins += 1
        else:
            print('Você PERDEU!')
            break
    else:
        if opcao in 'Ii':
            print('Você VENCEU!')
            wins += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-=' * 20)
print('-=' * 20)
print(f'GAME OVER! Você venceu {wins} vezes.')
