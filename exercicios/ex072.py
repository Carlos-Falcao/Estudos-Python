# Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa devera ler o número pelo teclado (entre 0 e 20) e mostrar por extenso.
# aula16

numExtenso = ("zero", "um", "dois", "três", "quatro", "cinco",
             "seis", "sete", "oito", "nove", "dez", "onze",
             "doze", "treze", "quatorze", "quinze", "dezesseis",
             "dezessete", "dezoito", "dezenove", "vinte")
while True:
    num = int(input('Digte um número entre 0 e 20: '))
    stay = ' '
    while num not in range(0, 21):
        num = int(input('Valor não aceito. Tente novamente um número entre 0 e 20: '))
    print(f'Você digitou o número {numExtenso[num]}')
    while stay not in 'SN':
        stay = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'N':
        break
print('Sistema Finalizado.')
