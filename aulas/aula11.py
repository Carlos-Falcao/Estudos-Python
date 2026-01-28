# Cores no Terminal

# Padrão ANSI - Padrão de Normalização Internacional
# Escape sequence - Funciona em varios ambientes

# Para representar uma cor sempre começar com "\033[...m"
# Entre o couchetes e o 'm' podem ir ate 3 valores: style, text, back.

# STYLE valores:
## 0 = None
## 1 = bold
## 4 = underline
## 7 = Negative (inverte as cores do fundo e a das letras)

# TEXT valores:
## 30 = Cinza
## 31 = Vermelho
## 32 = Verde
## 33 = Amarelo
## 34 = Azul
## 35 = Magenta
## 36 = Ciano
## 37 = Branco

# BACK valores:
## Mesmas ordem de cores do text, mas valores diferente.
## 40
## 41
## 42
## 43
## 44
## 45
## 46
## 47

# Ex: \033[0; 33; 44m  ou \033[33; 44m

print('\033[4;34mOla, mundo!\033[m')

a = 3
b = 5
print(f'Os valores são \033[33m{a}\033[m e \033[31m{b}\033[m!!!')

# Podemos criar um sistema de cores.
cores = {'limpo': '\033[m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'preto&branco': '\033[7;37m'
}
nome = 'Carlos'
print('Ola, muito prazer em te conhecer, {}{}{}'.format(cores['preto&branco'], nome, cores['limpo']))

# Desafios da aula:

# Inserir cores em 10 dos exercicios e no ex035 criar uma lista de cores.
