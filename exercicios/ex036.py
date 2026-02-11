# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. Pergunte o Valor da casa, o Salario do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salario ou então o emprestimo sera negado.
# aula12

valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
tempo = int(input('Quantos anos de financiamento: '))
prestacao = valorCasa / (tempo * 12)
minimo = salario * 0.30

print(f'Para pagar uma casa de R${valorCasa:.2f} em {tempo} anos a prestação sera de R${prestacao:.2f}')
if prestacao > minimo:
    print('Emprestimo NEGADO!')
else:
    print('Emprestimo CONCEDIDO!')
