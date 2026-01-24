# Receba um quantidade de Km percorridos por um carro e a quantidade de dias que ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
# aula07

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
total = (dias * 60) + (km * 0.15)

print(f'O total a pagar e de R${total:.2f}')
