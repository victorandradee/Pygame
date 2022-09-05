import pygame

pygame.init()
screen = pygame.display.set_mode((300,300))
pygame.display.set_caption("AULA 1 - EXERCICIO 1")
AZUL = (0, 0, 255)
BRANCO =(255, 255, 255)
AMARELO = (222, 191, 8)

screen.fill(AZUL)
pygame.draw.line(screen, BRANCO, (100, 0), (100, 300), 3)
pygame.draw.line(screen, BRANCO, (200, 0), (200, 300), 3)  
pygame.draw.line(screen, BRANCO, (0, 100), (300, 100), 3)
pygame.draw.line(screen, BRANCO, (0, 200), (300, 200), 3)


pygame.draw.circle(screen, AMARELO, (150,155), 20, 0)


pygame.display.flip()
pygame.time.delay(2000)

pygame.quit
