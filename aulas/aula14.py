# Estruturas/Laços de Repetições While (Parte 2)
# ex057 a ex065

# While executa sempre um bloco enquanto for verdadeiro.
# "Enquanto algo for verdadeiro, execute sempre esse bloco"

# Exemplo com passos e maçã da aula13.

"""
enquanto não maçã():
    passo()
pega()
"""

"""
while not maçã():
    passo()
pega()
"""

# Exemplo com um caminho sem um padrão.

"""
while not maçã():
    if chão:
        passo()
    if buraco:
        pula()
    if moeda():
        pega()
pega()
"""

# Pratica:
"""
for c in range(1, 10):
    print(c)
print('FIM')
"""
print('-=' * 20)

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

print('-=' * 20)

# Esse for e while tem o mesmo resultado.

# Exemplo com comando que espara um 0. Nesse exemplo não podemos usar o for.
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')

print('-=' * 20)

# Chamamos isso de 'Flag', ponto/condição de parada.

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N]: ')).upper()
print('FIM')

print('-=' * 20)

# Recebendo números pares e impares.

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Foram digitados {par} números pares e {impar} números impares!')
