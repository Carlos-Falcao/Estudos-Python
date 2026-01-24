# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# aula09

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu primeiro nome e {nome.split()[0]}')
print(f'Seu ultimo nome e {nome.split()[-1]}')

# OBS de possibilidades:

# Criar variável para o split.  -> nome = nome.split()
# Ultimo nome usando len.   -> {nome[len(nome) - 1]}
