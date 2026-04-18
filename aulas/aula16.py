# Variáveis Compostas (Tuplas)
# ex072 a ex077

# Em python existem 3 tipos de Variáveis Compostas: Tuplas, Listas e os Dicionarios.

# As Variáveis Simples é aquelas que usamos durante todo o mundo 1 e 2 de Python.
## Variáveis que usam 1 espaço na memoria.
# Porem com Tuplas/Listas/Dicionarios, podemos usar Variáveis Compostas, que usam mais de 1 espaço na memoria.

# Tupla.
# Podemos indentificar os elementos atravez do indice.
"""
petisco = hamburguer, suco, pizza, pudim
indice =     0        1      2      3
"""
# Strings são variáveis compostas.

petisco = ("hamburguer", "suco", "pizza", "pudim")
print(petisco[2])    # pizza
print(petisco[0:2])  # hamburguer e suco
print(petisco[1:])   # suco até o ultimo item, nesse caso: suco, pizza, pudim
print(petisco[-1])   # pudim
print(petisco[:2])   # hamburguer e suco

# Podemos usar o "len( )", onde podemos ver quantos elementos tem na variavel.
print(len(petisco))  # 4

# Podemos utilizar variáveis no loop for, por exemplo:
for c in petisco:
    print(c)

# AS TUPLAS SAO IMUTAVEIS.

## Ex:  petisco[1] = 'Refrigerante'
## Vai dar erro por conta que tuplas são imutaveis.

# () <- Tupla   OBS: apartir do python 3.5, não é mais preciso o parentese.
# [] <- Lista
# {} <- Dicionario

# Pratica:

print('\n\033[1;32mPRATICANDO\033[m')
lanches = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")
print('-=' * 20)
for comida in lanches:
    print(f'Eu vou comer {comida}')
print('Comi pra Caramba!')

print('--' * 20)
# Usando o len para o limite do for.
for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]} na posicao {cont}')

print('--' * 20)
# Os 2 método for acima tem o mesmo resultado.

# Nova maneira.
## "pos" recebe a posição  por conta do enumerate; 0 1 2.
## "comida" continua recebendo o valor; "Hamburguer" "Suco" "Pizza".
for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posicao {pos}')

print('--' * 20)
# Printando ele de maneira organizada, alfabética.
print(sorted(lanches))

print('--' * 20)
# Somando Tuplas.
a = (2, 4, 5, 7)
b = (1, 4, 6)
c = a + b
print(c)

# Ele junta as duas Tuplas, não soma e nem organiza.

print('--' * 20)
# Método "count" conta quantas vezes um valor apareceu dentro da tupla.
print(f'O numero 4 aparece {c.count(4)} na tupla.')   # 4 aparece 2 vezes.

print('--' * 20)
# "index" mostra em que posição se encontra o valor, porém só  o primeiro.
print(c)
print(c.index(4))

# print(c.index(4, 2)), como eu sei que o primeiro 4 aparece no index '1' eu peço  para ele procurar apartir do index '2'.

print('--' * 20)
# No python podemos usar tanto strings como int na mesma tupla.
pessoa = ('Carlos', 18, 'M', 56.8)
print(pessoa)

# Na tupla, não podemos mudar, porem podemos apagá-la.
del(pessoa)
# Porem não podemos apagar apenas 1 item, mas sim, apenas apagá-la inteira.
