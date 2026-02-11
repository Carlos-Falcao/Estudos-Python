# Crie um programa que leia o sexo de um pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente ate ter um valor correto. 
# aula14

sexo = str(input('Informe seu sexo [M/F]: ')).upper().strip()[0] # '[0]' Caso usuario digite "Masculino".

while sexo not in 'MF':
    sexo = str(input('Dados Invalidos! Por favor, informe seu sexo: ')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso!')
