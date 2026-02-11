# Melhore o ex061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disse que quer mostrar 0 Termos.
# aula14

# Meu método:
print('-=' * 10, 'Gerador de PA', '=-' * 10)

a1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contTermos = 0
termos = 10
while termos != 0:
    for i in range(1, termos + 1):
        print(f'{a1} -> ', end='')
        a1 += razao
        contTermos +=1
    print('PAUSA')
    termos = int(input('Quantos termos você quer a mais? '))
print(f'Progressão finalizada com {contTermos} termos mostrados.')

# Método Guanabara:
"""
print('-=' * 10, 'Gerador de PA', '=-' * 10)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
valor = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{valor} -> ', end='')
        valor += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
"""
