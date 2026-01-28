# Crie um programa que leia o comprimento de 3 retas e diga ao usuario se elas podem formar um triangulo.
# aula10

cores = {'limpar': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'azul': '\033[34m'
         }

print('{}-=-{}'.format(cores['vermelho'], cores['limpar']) * 10)
print('{}Analisador de Triangulos{}'.format(cores['verde'], cores['limpar']))
print('{}-=-{}'.format(cores['vermelho'], cores['limpar']) * 10)

a = float(input('Primeiro segmento: '))
b = float(input('Segunfo segmento: '))
c = float(input('Terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima {}PODEM FORMAR{} triangulo!'.format(cores['azul'], cores['limpar']))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} triangulo!'.format(cores['azul'], cores['limpar']))
