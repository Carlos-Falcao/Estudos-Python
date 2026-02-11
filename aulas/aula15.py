# Estruturas/Laços de Repetições While. (Parte 3)
# ex066 a ex071

# Interrompendo Repetições While.
# Exemplo da aula14, mais com trofeu e um loop infinito.
## trofeu = auto vitoria.
"""
while True:
    if chão:
        passo()
    if buraco:
        pula()
    if moeda():
        pega()
    if trofeu:
        pula()
        interrompa/break  <- Novo codigo
pega()
"""

# Comando break interrompe um loop.

# Pratica:
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
