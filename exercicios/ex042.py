# Refaça o ex035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# - Equilatero: Todos os lados iguais
# - Isoceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes
# aula12

# codigo ex035 com alterações.

cores = {'limpar': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'azul': '\033[34m'
         }

print('{}-={}'.format(cores['vermelho'], cores['limpar']) * 10)
print('{}Analisador de Triangulos{}'.format(cores['verde'], cores['limpar']))
print('{}-={}'.format(cores['vermelho'], cores['limpar']) * 10)

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('Os segmentos acima {}PODEM FORMAR{} um triangulo '.format(cores['azul'], cores['limpar']), end='')

    if l1 == l2 == l3:
        print('{}EQUILATERO.{}'.format(cores['verde'], cores['limpar']))
    elif l1 != l2 != l3 != l1:
        print('{}ESCALENO.{}'.format(cores['verde'], cores['limpar']))
    else:
        print('{}ISOCELES.{}'.format(cores['verde'], cores['limpar']))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} um triangulo.'.format(cores['azul'], cores['limpar']))
