# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# aula09

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu primeiro nome é \033[4;37m{nome.split()[0]}\033[m')
print(f'Seu ultimo nome é \033[4;31m{nome.split()[-1]}\033[m')

# OBS de possibilidades:

# Criar variável para o split.  -> nome = nome.split()
# Ultimo nome usando len.   -> {nome[len(nome) - 1]}
