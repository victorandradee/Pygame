import pygame
from pygame.locals import *
pygame.init()
SCREEN_SIZE = (400, 300)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Teste")
JogoAtivo = True
while JogoAtivo:
 # trata os eventos da fila de eventos
 for evento in pygame.event.get():
    print(evento)
    #verifica se o evento que veio eh para fechar a janela
    if evento.type == QUIT:
        JogoAtivo = False
    if evento.type == KEYDOWN:
        print('uma tecla foi pressionada')
    if evento.type == KEYUP:
        print('uma tecla foi liberada')