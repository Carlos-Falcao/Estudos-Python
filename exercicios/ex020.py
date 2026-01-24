# Um professor quer sortear a ordem da apresentação. Faça um programa que leia o nome de 4 alunos e mostre a ordem sorteada.
# aula08

from random import shuffle

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]

# Reembaralha a lista,      shuffle = embaralhar
shuffle(alunos)

print('A ordem selecionada foi ')
print(alunos)
