# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
# aula18

alunos = list()
pessoa = list()

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Nota 1: ')))
    pessoa.append(float(input('Nota 2: ')))
    alunos.append(pessoa[:])
    pessoa.clear()
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'N':
        break
print('-='*30)
print(f'{'No.':<5}{'NOME':<12}{'MÉDIA':>10}')
print('--'*20)
for x in range(0, len(alunos)):
    media = 0
    media = (alunos[x][1] + alunos[x][2]) / 2
    print(f'{x:<5}{alunos[x][0]:<12}{media:>10}')
print('--'*30)
while True:
    numAluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if numAluno == 999:
        break
    else:
        print(f'Notas de {alunos[numAluno][0]} são [{alunos[numAluno][1]}, {alunos[numAluno][2]}]')
        print('--'*30)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
