# Operadores Aritméticos
# ex005 a ex015

## Operador de adição  '+'
## Operador de subtração '-'
## Operador de multiplicação '*'
## Operador de divisão '/'
## Operador de potenciação '**'
## Operador de divisão inteira (A resposta da divisão sem valor com virgula)'//'
## Resto da divisão '%'

## '81 ** (1/2)' Raiz quadrada

## Ordem de Precedência
### 1- ()
### 2- **
### 3- *, /, //, %
### 4- +, -

resul = 3 * (5 + 4) ** 2 #243
print(resul)

## Teste

num1 = int(input('Digite um valor: '))
num2 = int(input('Digte outro valor: '))
s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2

print(f'A soma é {s}, o produto é {m} e a divisão é {d:.3f}', end=' >>> ')      # Deixa os prints na mesma linha
print(f'A divisao inteira é {di} e a exponenciação é {e}')
