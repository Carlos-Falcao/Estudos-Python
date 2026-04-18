# Variáveis Compostas (Dicionários)
# ex090 a ex095

# Para a criação de dicionários usamos:
# dados = dict()    ou
dados = {'nome': 'Pedro', 'idade': 25}
# 'Pedro' é o valor e 'nome' é o indicador do valor.

print(dados['nome'])    # 'Pedro'
print(dados['idade'])   # 25

# Para adicionar novas informações, append não funciona, para isso, basta fazer:
dados['sexo'] = 'M'
# Cria tanto o elemento 'sexo' como o valor 'M'.

# Para remover elementos, basta fazer:
del dados['idade']
# Perde tanto o dado como o elemento.

# Criando um dicionário filme.
filme = {'titulo': 'Star Wars',
         'ano': 1997,
         'diretor': 'George Lucas'
        }

# Para printar os valores da lista, use o comando:
print(filme.values())   # 'Star Wars', 1997, 'George Lucas'.

# Para printar as chaves da lista, basta fazer:
print(filme.keys())     # 'titulo', 'ano', 'diretor'.

# Para printar todos os itens, use o comando:
print(filme.items())    # ('titulo', 'Star Wars'), ('ano', 1997), ('diretor', 'George Lucas').

print('--'*20)
# Posso usar essas funções para laços de repetições, como o while ou o for.
for chave, valor in filme.items():
    print(f'O {chave} é {valor}')
print('--'*20)

# Também posso fazer uma lista armazenar um dicionário, como por exemplo:
locadora = ({'titulo': 'Star Wars', 'ano': 1997, 'diretor': 'George Lucas'},
            {'titulo': 'Avengers', 'ano': 2012, 'diretor': 'Joss Whedon'},
            {'titulo': 'Matrix', 'ano': 1999, 'diretor': 'Wachowski'})
print(locadora[0]['ano'])   # 1997
print(locadora[2]['titulo'])    # 'Matrix

# Pratica:

print('-='*30)
print('PRATICA')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
pessoas['nome'] = 'Leandro'     # Mudou de 'Gustavo' para 'Leandro'.
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('--'*20)
# Salvando dicionários em uma lista.
"""
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['uf'])
"""

# Agora fazendo o mesmo código, mas com o usuário digitando os valores e salvando dentro de uma lista usando o comando copy().
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())    # O método estado[:] não funciona com dicionários.
# print(brasil) Para printar de uma maneira melhor de se ver, basta usar um for.
for e in brasil:   # Acessa a lista.
    for valor in e.values():    # Acessa o dicionário.
        print(valor, end=' ')
    print()
