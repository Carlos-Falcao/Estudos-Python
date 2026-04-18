# Crie um programa que o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo devera analisar se a expressão passada esta com parênteses abertos e fechados na ordem correta.
# aula17

# Método Guanabara:
expressao = str(input('Digite sua expressão: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão esta errada!')

# Meu método:
## Esta incorreto, porem queria salvar para perceber meu erro.
## ((a+b)-2())  <- Esta vindo como Expressão correta.
"""
expressao = str(input('Digite sua expressão: '))
abertos = fechados = 0
for letra in expressao:
    if letra == '(':
        abertos += 1
    elif letra == ')':
        fechados +=1
if abertos == fechados:
    print('Sua expressão esta correta!')
else:
    print('Sua expressão esta errada!')
"""
