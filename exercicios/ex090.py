# Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
# aula19

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] <= 5.9:
    aluno['situação'] = 'Reprovado'
elif aluno['media'] <= 6.9:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'
print('-='*30)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
