# Crie um programa que vai ler vários números e colocalos em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma descrescente.
# C) Se o valor 5 foi difitado e esta ou não na lista.
# aula17

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while stay not in 'SN':
        stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'N':
        valores.sort(reverse=True)
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
