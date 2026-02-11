# Refaça o ex051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
# aula14

print('-=' * 10, 'Gerador de PA', '=-' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
valor = a1
cont = 1
while cont <= 10:
    print(f'{valor} -> ', end='')
    valor += r
    cont += 1
print('FIM')
