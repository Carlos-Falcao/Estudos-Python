# Condições Aninhadas
# ex036 a ex045

# Uso do elif.
# Elif faz o 'Senão se', criando uma nova coluna de possibilidades.

"""
if carro.esquerda():
    bloco_1
elif carro.direita():
    bloco_2
else:
    bloco_3
"""

# Não existe um limite de quantos elif utilizar.

# Estrutura condicional aninhada:
nome = str(input('Qual o seu nome? '))
if nome == 'Carlos':
    print('Que nome bonito.')
elif nome == 'Gustavo' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Heloisa Julia Maria':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, \033[1;31m{nome}\033[m!')
