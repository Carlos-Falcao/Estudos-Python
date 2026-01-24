# faça um Input para ser inserido 'algo' e depois mostre as informações desse 'algo'.
# aula06

algo = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético? ', algo.isalpha())
print('É alfanumérico? ', algo.isalnum())
print('Está em maiusculas? ', algo.isupper())
print('Está em minusculas? ', algo.islower())
print('Está capitalizada? ', algo.istitle()) # Maiusculas e minusculas
