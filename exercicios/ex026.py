# Faça um Programa que leia uma frase pelo teclado e mostre:
# -> Quantas vezes apareceu 'A'.
# -> Em que posicao ela apareceu a primeira vez.
# -> Em que posicao ela apareceu a ultima vez.

# aula09

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A primeira letra A apareceu na posicao {frase.find('A') + 1}')
print(f'A ultima letra A apareceu na posicao {frase.rfind('A') + 1}')
