# Condições Simples e Compostas
# ex028 a ex035

# Uso de if else.
# Uso de possibilidades/condições no código.

# Exemplo com carro em movimento.

"""
carro.siga()
Se carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
senao:
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
carro.pare()
"""

# Exemplo:
tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')

# Ou
#   print('Carro Novo' if tempo <= 3 else 'Carro Velho')

# Estrutura de condição simples:
## Quando o else não é necessario.

nome = str(input('Qual é seu nome? '))

"""
if nome == 'Carlos':
    print('Belo nome você tem!')
print(f'Bom dia, {nome}!')
"""

# Agora com estrutura composta:

if nome == 'Carlos':
    print('Belo nome você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
