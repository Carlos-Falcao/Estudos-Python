# Faça um Programa que leia uma frase pelo teclado e mostre:
# -> Quantas vezes apareceu 'A'.
# -> Em que posicao ela apareceu a primeira vez.
# -> Em que posicao ela apareceu a ultima vez.

# aula09

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'A letra A aparece \033[1;32m{frase.count('A')}\033[m vezes na frase.')
print(f'A primeira letra A apareceu na posicao \033[1;36m{frase.find('A') + 1}\033[m')
print(f'A ultima letra A apareceu na posicao \033[1;31m{frase.rfind('A') + 1}\033[m')
