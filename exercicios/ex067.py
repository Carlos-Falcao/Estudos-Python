# Crie um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuario.
# O programa sera interrompido quando o número solicitado for negativo.
# aula15

while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('---' * 10)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} X {i:2} = {num * i}')
    print('---' * 10)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
