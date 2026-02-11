# Receba um número e mostre sua tabuada.
# aula07

n = int(input('Digite um número: '))

# Método do video foi outro.

print('-' * 13)

for i in range(1, 11):
    res = n * i
    print(f'{n} X {i:2} = {res}')

print('-' * 13)

# OBS: O Método para resolver esse ex era outra, o método utilizado é o mesmo do ex049.
