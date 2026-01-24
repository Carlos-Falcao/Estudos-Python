# Receba em R$ o preço de um produto e mostre ele com um desconto de 5%.
# aula07

prec = float(input('Qual o preço do produto? R$'))
newPrec = prec - (prec * 0.05)  # Ou prec - (prec * 5 / 100)

print(f'O produto que custava R${prec:.2f}, na promoção com desconto de 5% vai custar R${newPrec:.2f}')
