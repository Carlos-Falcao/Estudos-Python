# Funções (Parte 1)
# ex096 a 106

# Para criar uma função em python, usamos o comando 'def' que significa 'Definição de função'.
# Funções podem ser vista como uma rotina.
def mostraLinha():
    print('--'*30)


# Programa Principal
mostraLinha()
print(f'{'OLÁ MUNDO!':^60}')

# def também pode trabalhar com parâmetros.
# Exemplo:
def mensagem(msg):
    mostraLinha()
    print(f'{msg:^60}')
    mostraLinha()


mensagem('SISTEMA DE ALUNOS')   # Passei o parâmetro 'msg'.

# Pratica:

print('-='*30)
print('PRATICA')

def soma(a, b):
    mostraLinha()
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal
soma(4, 5)
soma(b=8, a=9)
soma(2, 1)

mostraLinha()
# Aprendendo a 'Empacotar Parâmetros'.
# O '*num' significa que estamos falando para o python que não sabemos quantos valores ele vai receber, pode ser 2 ou mais.
def contador(*num):
    """
    for valor in num:
        print(f'{valor}', end=' ')
    print('FIM!')
    """ # Ou
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

mostraLinha()
# Função para dobra números de uma lista.
valores = [7, 2, 5, 0, 4]
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


print(valores)
dobra(valores)
print(valores)
