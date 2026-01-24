# Receba um salário e mostre ele com o aumento de 15%.
# aula07

sala = float(input('Qual é o salário do Funcionario? R$'))
newSala = sala + (sala * 15 / 100)

print(f'Um funcionario que ganhava R${sala:.2f}, com 15% de aumento, passa a receber R${newSala:.2f}')
