# Crie um programa que leia o nome e o Preço de varios produtos. O programa devera perguntar se o usuario vai continuar. No final, mostre:
# A) O total gasto na compra.
# B) Quantos produtos custam mais de R$1000.00
# C) O nome do produto mais barato.
# aula15

print('---' * 10)
print('LOJAS SUPER')
print('---' * 10)

totCompra = prodMais1k = maisBarato = 0
nomeProdBarato = ' '
while True:
    nomeProd = str(input('Nome do Produto: ')).strip()
    precProd = float(input('Preço: R$'))
    totCompra += precProd
    if precProd >= 1000:
        prodMais1k += 1
    if maisBarato == 0 or precProd < maisBarato:
        maisBarato = precProd
        nomeProdBarato = nomeProd
    stay = ' '
    while stay not in 'SN':
        stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^40}')
print(f'O total da compra foi R${totCompra:.2f}')
print(f'Temos {prodMais1k} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeProdBarato} que custa R${maisBarato:.2f}')
