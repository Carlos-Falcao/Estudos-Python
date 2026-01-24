# Um professor sorteará 1 dos seus 4 alunos pra apagar o quadro. Faça um programa que leia seus nomes e escreva o nome do escolhido.
# aula08

from random import choice

aluno1 = input('Digite o nome do aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]

# Escolhe um aluno aleatorio da lista
print(f'O aluno sortedo foi {choice(alunos)}.')
