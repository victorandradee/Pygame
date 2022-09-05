import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("CÍRCULOS")
JogoAtivo = True
while JogoAtivo: 
 for evento in pygame.event.get():
    if evento.type == QUIT:
        JogoAtivo = False
    if evento.type == MOUSEBUTTONDOWN:
        x1,y1 = pygame.mouse.get_pos()
        pygame.draw.circle(screen,(255, 255, 255),(x1, y1),50, 0)
 
 pygame.display.flip() 
pygame.time.delay(2000)
pygame.quit()
