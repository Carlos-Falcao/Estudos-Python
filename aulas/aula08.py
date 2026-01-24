# Utilizando Módulos
# ex016 a ex021

# Para ver as possiveis bibliotecas para baixar vá em 'python.org>docs'
# import 'Ctrl + espaco' mostra as bibliotecas padrão

## Como importar Bibliotecas(Módulos)
## Partes adicionais que podemos inserir no nosso código.
## Em Python utilizamos: import bebidas, import doce, import etc.
## Também podemos importar coisas específicas para melhor uso do armazenamento: from doce import pudin, from bebidas import agua.

## Exemplo da biblioteca 'math'
### Na biblioteca 'math' temos o 'ceil' que arredonda um valor para cima, e 'floor' que arredonda pra baixo.
### Temos 'trunc', que vai eliminar os valores da virgula para frente, sem arredondar.
### 'sqrt' SquareRoot serve para calcular a raiz quadrada.
### 'factorial' calcula o fatorial de um valor.

### Se importar a biblioteca inteira, para utiliza algo use: 'math.sqrt(valor)'
### Se importar apenas uma funcao especifica não precisa do 'math.algo()', apenas a função como no código abaixo.

### EX:

# 'import math' para importar tudo
from math import sqrt, ceil

num = int(input('Digite um numero: '))
raiz = sqrt(num)

print(f'A raiz de {num} é igual a {ceil(raiz)}')

## Exemplo de outra Biblioteca, 'random'
### Podemos usar para pegar valores aleatórios entre outras funções.
### 'random' gera um valor aleatório.
### 'randint(1, x)' gera um valor aleatório entre os valores definidos no parênteses .

# Exemplo com biblioteca 'random'
import random

num2 = random.randint(1, 10) # Valor aleatório inteiro entre 1 e 10
print(num2)

