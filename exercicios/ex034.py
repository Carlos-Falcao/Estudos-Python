# Escreva um programa que leia o salario de um funcionario e calcule o valor do aumento.
# Para salarios superiores a R$1250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento sera de 15%.
# aula10

sala = float(input('Qual o salario do funcionario? R$'))

if sala <= 1250:
    newSala = sala + (sala * 0.15)
else:
    newSala = sala + (sala * 0.10)

print(f'Quem ganhava \033[1;31mR${sala:.2f}\033[m passa a ganhar \033[1;32mR${newSala:.2f}\033[m agora.')
