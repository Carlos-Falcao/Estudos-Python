# Crie um programa que tenha uma tupla com varias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
# aula16

# Utilizei as mesmas palavras do video do ex077.
texto = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in texto:
    print(f'\nNa palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            vogal = letra.lower()
            print(vogal, end=' ')
