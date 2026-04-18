# Variáveis Compostas (Listas) Parte 1
# ex078 a ex083

# Primeira diferença entre tuplas e listas; Listas não são imutaveis.
# Para listas são usados [ ].

lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
# Alterando um valor da lista.
lanche[3] = 'sorvete'

# Para add novos itens no final das listas, usamos o comando 'append(nomeObjeto)'.
lanche.append('cookies')
# Para add um novo item em uma posição especifica, usamos o 'insert(posição, nomeObjeto)'.
lanche.insert(0, 'cachorro quente')
# Para apagar itens de uma listas, ha varias maneiras.
## del lanche[3]
## lanche.pop(3)    -> Normalmente usado para apagar o ultimo elemento, mas também podemos passar o index.
## lanche.remove('pizza')   -> Não passamos o index, mas sim o valor que queremos eliminar.
del lanche[3]
lanche.pop()

# Para verificar se temos um elemento na lista, podemos usar o 'if in'.
if 'pizza' in lanche:
    lanche.remove('pizza')

print(lanche)

# Podemos criar listas atravez de range.
numeros = list(range(4, 11))    # -> Resul: [4, 5, 6, 7, 8, 9, 10]
## A função list serve para declarar uma lista.

# Se possuirmos uma lista com valores fora de ordem, podemos usar a função sort() para organizá-los.
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
# Para criarmos ele ao contrario, basta fazer:
valores.sort(reverse = True)

# Para saber o número de valores em uma lista, basta usar o len().
len(valores)    # 7, para mostrar é só usar o print.

# Pratica:

print('-=' * 20)
print('PRATICA')

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.remove(2)   # Podemos notar que ele vai remover apenas o primeiro elemento de valor '2'.
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')

# Novo teste com lista vazia, mostrando a lista de maneira mais 'bonita'.
print('-=' * 20)

teste = []  # Posso colocar como: teste = list()
teste.append(5)
teste.append(9)
teste.append(4)

print(teste)
# For para mostrar a lista.
## enumerate pega tanto a posição como o valor.
for c, x in enumerate(teste):
    print(f'Na posição {c} temos o valor {x}...')
print('Cheguei ao final da lista.')

# Também podemos usar o for para add elementos a uma lista.
print('-=' * 20)

elementos = list()
for cont in range(0, 5):
    elementos.append(int(input('Digite um número inteiro: ')))
for c, i in enumerate(elementos):
    print(f'Na posição {c} temos o valor {i}!')
print('Cheguei ao final da lista.')

# Também podemos ligar duas listas.
## Mas Cuidado, ao fazer isso, se alterar uma, altera a outra.
print('-=' * 20)

a = [2, 3, 4, 7]
b = a
b[2] = 8    # Pedi para alterar apenas a lista 'b'. Porém, alterou a lista 'a' também.
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Para evitar criar uma ligação entre as duas e apenas fazer uma cópia, basta fazer do seguinte jeito:
b = a[:]
