# Receba Altura e Largura de uma Parede, calcule sua área e quanta Tinta precisara para pintala inteira.    2m = 1L de Tinta
# aula07

wallAlt = float(input('Altura da parede: '))
wallLarg = float(input('Largura da parede: '))
area = wallAlt * wallLarg
Ltinta = area / 2

print(f'Sua parede tem a dimensao de {wallAlt}X{wallLarg} e sua área é de {area}m.')
print(f'Para pintar essa parede, você precisara de {Ltinta}L de tinta.')
