# Faça um Programa que leia um angulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse angulo.
# aula08

from math import sin, cos, tan, radians

ang = float(input('Digite um Angulo qualquer: '))
rad = radians(ang)

print(f'Seu SENO é {sin(rad):.2f}')
print(f'Seu COSSENO é {cos(rad):.2f}')
print(f'Sua TANGENTE é igual a {tan(rad):.2f}')
