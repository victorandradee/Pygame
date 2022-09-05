import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("FERRARI")
JogoAtivo = True
fundo = "imagens/corrida.png"
imagem = "imagens/ferrari1.png"
imagem2 = "imagens/ferrari2.png"
imagem3 = "imagens/gameover.jpg"

gameover = pygame.image.load(imagem3)
background = pygame.image.load(fundo)
carro = pygame.image.load(imagem)
carro2 = pygame.image.load(imagem2)
X = 1
Y = 50

volta = 0
while JogoAtivo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False
    pygame.display.update()
    screen.blit(background, (0, 0))
    if evento.type == pygame.KEYDOWN:
        if volta == 0:
            if evento.key == pygame.K_RIGHT:
                X+= 10
                screen.blit(carro, (X, Y))

        elif volta == 1:
            if evento.key == pygame.K_RIGHT:
                    X-= 10
                    screen.blit(carro2, (X, Y))
                    pygame.display.update()


        if X == 801 and Y == 50:
            pygame.display.update()
            Y+=250
            volta = 1
        if X == -19:
            Y += 250
            volta = 0
        if X == 901:
            screen.blit(gameover, (330, 300))
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()
            

