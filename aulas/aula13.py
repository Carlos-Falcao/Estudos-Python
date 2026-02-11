# Estruturas/Laços de Repetições for (Parte 1)
# ex046 a ex056

# for serve para repetir um bloco de código .

# Exemplo com passos:
"""
laço c no intervalo(1, 10)
    passo()
pega()
"""

"""
for c in range(1, 10):
    print(c)
"""

# Exemplo com if:
"""
laço c no intervalo(0, 3)
    se moeda():
        pega
    passo()
    pula()
passo()
pega()
"""

# Pratica:
for c in range(1, 7):
    print(c)
print('FIM')

print('-=' * 20)

# Fazendo contagem ao contrario
# for c in range(6, 0, -1) -> O terceiro valor e a iteração, ou seja, vai tirar 1.

for c in range(6, 0, -1):
    print(c)
print('FIM')

print('-=' * 20)

for c in range(0, 7, 2):
    print(c)
print('FIM')

print('-=' * 20)

# Exemplo recebendo um input.
n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(f'Valor igual a {c}')
print('FIM')

print('-=' * 20)

# Exemplo recebendo o inicio, fim e o passo.
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

print('-=' * 20)

# Somando valores
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n      # s = s + n
print(f'A soma total foi de {s}')
