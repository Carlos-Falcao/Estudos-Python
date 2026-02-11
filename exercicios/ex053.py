# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# EX: O lobo ama o bolo -> olob o ama obol o
# aula13

# Meu método:
# Não usei o for.

"""
frase = str(input('Digte uma frase: ')).strip().upper()
frase = frase.replace(" ", "")
fraseInversa = frase[::-1]
print(f'O inverso de {frase} é {fraseInversa}')
if frase == fraseInversa:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo')
"""

# Método do Guanabara: 

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()    # Transforma a frase em uma lista
junto = ''.join(palavras)   # Junta as palavras sem espaços
inverso = ''

for letra in range(len(junto) - 1, -1, -1):   # range(pega a ultima letra; para ir ate a ultima letra; indo de -1 em -1)
    inverso += junto[letra]

print(f'O inverso de {frase} é {inverso}')
if junto == inverso:
    print('Temos um palindromo!')
else:
    print('Não temos um palindromo')
