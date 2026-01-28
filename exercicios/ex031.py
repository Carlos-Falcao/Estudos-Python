# Desenvolva um programa que pergunta a distancia de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de ate 200Km e R$0.45 para viagens mais longas.
# aula10

dis = float(input('Qual a distancia da sua viagem? '))

print(f'Você esta prestes a fazer uma viagem de {dis}Km.')

if dis > 200:
    preco = dis * 0.45
else:
    preco = dis * 0.50

print(f'E o preço da sua passagem sera de \033[7;37mR${preco:.2f}\033[m')

# Metodo In-line
# preco = dis * 0.50 if dis <= 200 else preco = dis * 0.45
