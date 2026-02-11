# Refaça o ex009, mostrando a tabuada de um número, só que agora utilizando um laço for.
# aula13

n = int(input('Digte um número para ver sua tabuada: '))

for i in range(1, 11):
    print(f'{n} X {i:2} = {n*i}')
