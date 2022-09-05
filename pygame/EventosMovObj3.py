import pygame
from random import randint
pygame.init()
largura = 640
altura = 480
tamanho = 10
# posição aleatória (dentro da tela) para o quadrado aparecer
posicao_x = randint(0, (largura - tamanho))
posicao_y = randint(0, (altura - tamanho))
# para dar velocidade ao quadrado
velocidade_x = 0
velocidade_y = 0
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Movimentação de objetos")
janela.fill((255, 255, 255))
deve_continuar = True
while deve_continuar:
 # Checando eventos que estão ocorrendo neste momento
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        deve_continuar = False
    # Se uma tecla for pressionada
    if event.type == pygame.KEYDOWN:
    # Se a tecla for a seta para a esquerda
        if event.key == pygame.K_LEFT:
            velocidade_y = 0
            velocidade_x = -0.05
        # Se a tecla for a seta para a direita
        if event.key == pygame.K_RIGHT:
            velocidade_y = 0
            velocidade_x = 0.05
        # Se a tecla for a seta para cima
        if event.key == pygame.K_UP:
            velocidade_x = 0
            velocidade_y = -0.05
        # Se a tecla for a seta para baixo
        if event.key == pygame.K_DOWN:
            velocidade_x = 0
            velocidade_y = 0.05

    pygame.draw.rect(janela, (0, 0, 0), (posicao_x, posicao_y, 
    tamanho, tamanho))
    posicao_x += velocidade_x
    posicao_y += velocidade_y
    pygame.display.flip()
pygame.quit()
