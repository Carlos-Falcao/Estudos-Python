# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.
# aula10

vel = float(input('Qual a velocidade atual do carro? '))

if vel > 80:
    print('\033[1;31mMULTADO! Você excedeu o limite permitido de 80Km/h')
    multa = (vel - 80) * 7
    print(f'Você deve pagar um multa de R${multa:.2f}\033[m')

print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')
