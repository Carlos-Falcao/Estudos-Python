# Tipos Primitivos e Saida de Dados
# ex001 a ex004

## int = 7, -4, 0, 9973
## float = 4.5, 0.073, -15.223, 7.0
## bool = True, False
## str = 'Ola', '7.5', ''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))     # Ou print(f'A soma entre {n1} e {n2} vale {s}')
print(type(n1))

# Teste 2

n = input('Digite algo: ')
print(n.isnumeric()) # é numero?
print(n.isalpha()) # é letra?
print(n.isalnum()) # é letra e/ou numero?
print(n.isupper()) # é somente letras maiuscola?
print(n.islower()) # é somente letras minuscola?
print(n.isprintable()) # pode ser impresso?
