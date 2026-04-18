# Crie um  programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
# aula19

from datetime import date

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (date.today().year - pessoa['contratação']))
print('-='*30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
