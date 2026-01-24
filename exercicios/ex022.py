# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiusculas e minusculas.
# -> Quantas letras ao todo (sem considerar espaços).
# -> Quantas letras tem o primeiro nome.

# aula09

nome = str(input('Digite seu nome completo: ')).strip()     # Remove os espaços desnecessarios

print('Analisando seu nome...')
print(f'Seu nome em maiusculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras')

nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e ele tem {len(nome[0])} letras')
# Ou para descobrir a quantidade de letra, podemos fazer:  print(f'Seu primeiro nome tem {nome.find(' ')} letras)
