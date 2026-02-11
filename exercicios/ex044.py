# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - 2X no cartão: preço normal
# - 3X ou mais no cartão: 20% de juros
# aula12

print('\033[1;32m{:=^57}\033[m'.format(' LOJAS DO FALCAO '))

preco = float(input('Preço das compras: R$'))

print('''\033[33mFORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão\033[m''')

opcao = int(input('Sua opção: '))
if opcao == 1:
    total = preco - (preco * 0.10)
    print('à vista no dinheiro/cheque, sua compra tera um desconto de 10%.')
elif opcao == 2:
    total = preco - (preco * 0.05)
    print('à vista no cartão, sua compra tera um desconto de 5%.')
elif opcao == 3:
    total = preco
    parcelasvalor = preco / 2
    print(f'Sua compra sera parcelada em 2X de R${parcelasvalor:.2f} SEM JUROS.')
elif opcao == 4:
    parcelas = int(input('Você quer parcelar em quantas vezes? '))
    total = preco + (preco * 0.20)
    parcelasvalor = total / parcelas
    print(f'Sua compra sera parcelada em {parcelas}X de R${parcelasvalor:.2f} COM JUROS.')
else:
    total = 0
    print('\033[1;31mOpção Invalida, tente novamente!\033[m')

print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')
