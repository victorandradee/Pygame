import pygame

pygame.init()

VERDE = (0, 255,0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
AMARELO = (222, 191, 0)
PRETO = (0, 0 ,0)
VERMELHO = (255, 0, 0)

opc = 0
print ('Escolha a bandeira que você deseja visualizar: ')
print ((' - GUINÉ'))
print ((' - ALEMANHA'))
print ((' - LAOS'))
while (opc < 1 or opc> 3):
    opc = int (input('Informe sua opção: '))

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('AULA 1 - EXERCÍCIO 2')
screen.fill(BRANCO)
if opc == 1:
    pygame.draw.rect(screen, VERMELHO, (30, 100, 80, 100), 0)
    pygame.draw.rect(screen, AMARELO, (110, 100, 80, 100), 0)
    pygame.draw.rect(screen, VERMELHO, (190, 100, 80, 100), 0)

if opc == 2:
    pygame.draw.rect(screen, PRETO, (75, 60, 150, 60), 0)
    pygame.draw.rect(screen, AMARELO, (75, 120, 150, 60), 0)
    pygame. draw.rect(screen, VERMELHO, (75, 100, 150, 60), 0)

if opc == 3:
    pygame.draw.rect(screen, VERMELHO, (75, 60, 150, 40), 0)
    pygame.draw.rect(screen, AZUL, (75, 100, 150, 100), 0)
    pygame.draw.rect(screen, VERMELHO, (75, 100, 150, 40), 0)
    pygame.draw.circle(screen, BRANCO, (150, 140), 20, 0)

pygame.display.flip()
pygame.time.delay(4000)

pygame.quit()
