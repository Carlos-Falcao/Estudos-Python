# Crie um programa que tenha uma tupla unica com nome de produtos e seus respectivos precos, na sequencia.
# No final, mostre uma listagem de precos, organizando os dados em forma tabular.
# aula16

produtos = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32,
            'Canetas', 22.30, 'Livro', 34.90)
print('---' * 20)
print(f'{'LISTAGEM DE PRECOS':>38}')
print('---' * 20)
for pos, x in enumerate(produtos):
    if pos % 2 == 0:
        print(f'{x:.<52}', end='')
    else:
        print(f'R$ {x:>6.2f}')
print('---' * 20)

# O método for do Guanabara, embora parecido, foi diferente:
"""
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{x:.<52}', end='')
    else:
        print(f'R$ {x:>6.2f}')
"""
# Usou o range e como limite utilizou o len(produtos).
