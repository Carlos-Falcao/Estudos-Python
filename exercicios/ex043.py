# Desenvolva um logica que leia o peso e altura de uma pessoa, calcule se IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - Entre 25 e 30: Sobrepeso
# - Entre 30 e 40: Obesidade
# - Acima de 40: Obesidade Morbida
# aula12

peso = float(input('Qual o seu peso? (Kg) '))
alt = float(input('Qual a sua altura? (m) '))
imc = peso / (alt ** 2) # ou (alt * alt)

print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Abaixo do Peso, cuidado!')
elif 18.5 <= imc < 25:
    print('PARABENS! Você esta no peso ideal!')
elif 25 <= imc < 30:
    print('Você esta com Sobrepeso, cuidado!')
elif 30 <= imc < 40:
    print('CUIDADO, você esta Obeso!')
else:
    print('MUITO CUIDADO! Você esta com Obesidade Morbida!')
