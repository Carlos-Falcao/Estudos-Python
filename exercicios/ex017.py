# Faça um Programa que leia o comprimento do Cateto Oposto e do Cateto Adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
# aula08

from math import hypot

catOposto = float(input('Digite o valor do cateto Oposto: '))
catAdjancente = float(input('Digite o valor do cateto Adjacente: '))
hipotenusa = hypot(catOposto, catAdjancente)

print(f'A hipotenusa do triangulo é igual a {hipotenusa:.2f}.')

# Metodo sem biblioteca

# co = float(input('Digite o valor do cateto Oposto: '))
# ca = float(input('Digite o valor do cateto Adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)                             --> Soma dos quadrados dos catetos igual ao quadrado da hipoteusa

# print(f'A hipotenusa do triangulo é igual a {hi:.2f}.')
