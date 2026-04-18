# Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
# aula17

nums = []
cont = 0
while True:
    nums.append(int(input('Digite um valor: ')))
    if cont == 0:
        print('valor adicionado com sucesso...')
    else:
        temIgual = False
        for x in range(0, len(nums) - 1):
            if nums[x] == nums[-1]:
                temIgual = True
                nums.pop()
                break
            else:
                temIgual = False
        if temIgual:
            print('Valor duplicado! Não vou adicionar...')
        else:
            print('valor adicionado com sucesso...')
    stay = ' '
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay not in 'SN':
        stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'N':
        break
    cont += 1
print('-=' * 30)
nums.sort()
print(f'Você digitou os valores {nums}')

# Método Guanabara:
# Bem melhor que o meu :(
"""
nums = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in nums:
        nums.append(n)
        print('valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'N':
        break
print('-=' * 30)
nums.sort()
print(f'Você digitou os valores {nums}')
"""
