# Faça um programa que abra e reproduza o audio de um arquivo MP3.
# aula08

# Biblioteca pygame
import pygame

# Inicializa todos os modulos pygame importados
pygame.init()

# Inicializa so o mixer pygame
# pygame.mixer.init()

# Carrega um arquivo de musica para a reproducao
pygame.mixer.music.load('ex021.mp3')

# Inicializa a reproducao do fluxo de musica
pygame.mixer.music.play()

input()
pygame.event.wait()
