# Receba o valor de dinheiro na carteira em Reais, mostre quanto terá em Doláres.    R$1 = US$3.27
# aula07

Rs = float(input('Quanto dinheiro vc tem na carteira? R$'))
Dl = Rs / 3.27

print(f'Com R${Rs:.2f} vc pode comprar US${Dl:.2f}')
