# Manipulando Cadeias de Texto
# ex022 a ex027

# Aprendendo sobre String.
# Espaços e Indice dos micros espaços de memória.
## Ex: 'Ola Mundo'; começa no indice 0 e vai ate o fim da frase/palavra.
## Ex: indice 2 = 'a', indice 3 = ' ', indice 0 = 'O'.


# Fatiamento de String

frase = 'Curso em Video Python'     # -> frase de indice 0 a 20;    21 total somando com o 0.
print(frase[9])

## frase[9:13] -> Pega todos os valores de 9 a 12, o 13/ultimo valor não conta.
## frase[9:21:2] -> Pula de dois em dois valores; = 'V,d,o,P,t,o'.
## frase[:5] -> mesma coisa que frase[0:5] = 'Curso'
## frase[15:] -> Pega o valor da casa 15 até a última casa; = 'Python'
## frase[9::3] -> Começa no valor 9 e vai até o final pulando 3 casas; = 'V,e,P,h'.
## frase[::2] -> Mostra a string inteira pulando de 2 em 2.


# Análise de String

len(frase)      # -> 'len' de length, tamanho/comprimento

frase.count('o')       # -> Vai contar o número de vezes do 'o' minusculo.

## frase.count('o',0,13) -> Vai contar os 'o' dentre o indice 0 ate o 12.

frase.find('deo')      # -> Vai indicar o indice que começa o 'deo' = 11.

## frase.find('Android') -> Retornara o valor '-1' pq o valor de 'Android' não existe.

'Curso' in frase       # -> Retornará 'True', pois existe 'Curso' na frase.


# Transformação de String

frase.replace('Python', 'Android')      # -> Substituirá a palavra 'Python' por 'Android'.

## Não substitui para sempre, apenas no momento, e preciso salvar a nova frase na variável de novo.
## frase = frase.replace('Python', 'Android')

frase.upper()       # -> Vai deixar a frase inteira em maiusculas.

## frase.lower() -> Transforma para minusculas
## frase.capitaliza() -> Deixa todos os caracteres em minusculas, menos a primeira letra de cada palavra.   Antes -> 'curso em video python'; Depois -> 'Curso em Video Python'
## frase.title() -> Análisa as quebras(espaços) de palavras e deixa todas as letra após a quebra maiusculas.     Antes -> 'curso em video python'; Depois -> 'Curso Em Video Python'
## frase.strip() -> Remove os espaços inuteis.      EX: Antes -> '   Aprenda Python  '; Depois -> 'Aprenda Python'
## frase.rstrip() -> 'r' de 'Right'; Remove somente os espaços da direita.
## frase.lstrip() -> 'l' de 'Left'; Remove somente os espaços da esquerda.


# Divisão de String

frase.split()       # -> Ocorre uma divisão dentre os espaços.

## Transforma a frase em uma lista.
## EX -> ['Curso', 'em', 'Video', 'Python']

'-'.join(frase)     # -> Juntaria a frase de novo com o '-' fazendo a separação.

## EX -> 'Curso-em-Video-Python'.


# Quando se quise escrever um texto grande, para evitar muitos prints, use """ """ aspas tripla, na quebra de linha ele já mostra assim.

print("""De que são feitos os dias?
- De pequenos desejos,
vagarosas saudades,
silenciosas lembranças.

Entre mágoas sombrias,
momentâneos lampejos:
vagas felicidades,
inatuais esperanças.

De loucuras, de crimes,
de pecados, de glórias
- do medo que encadeia
todas essas mudanças.

Dentro deles vivemos,
dentro deles choramos,
em duros desenlaces
e em sinistras alianças...""")
