# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: APROVADO
# aula12

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

print(f'Tirando {n1:.2f} e {n2:.2f}, a média do aluno é {m:.2f}')
if m < 5:
    print('\033[31mO alunos esta REPROVADO.\033[m')
elif m <= 6.99:
    print('\033[33mO aluno esta de Recuperação.\033[m')
else:
    print('\033[32mO aluno esta APROVADO.\033[m')

# Exemplo de recuperacao primeiro:

'''
if 7 > m >= 5:
    ...
elif m < 5:
    ...
elif m >= 7:    <- jeito para deixar o codigo mais legivel
    ...
'''
