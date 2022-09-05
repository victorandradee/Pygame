import pygame
# inicializa o pygame
pygame.init()
largura = 640
altura = 480
posicao_x = int(largura / 2)
posicao_y = int(altura / 2)
tamanho = 10
# Criando uma janela com o título "Movimentação de objetos"
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Movimentação de objetos")
deve_continuar = True
# Loop do jogo
while deve_continuar:
 # Checando eventos que estão ocorrendo neste momento
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        deve_continuar = False
 janela.fill((255, 255, 255))
 pygame.draw.rect(janela, (0, 0, 0), (posicao_x, posicao_y, 
tamanho, tamanho))
 posicao_x += 1
 pygame.time.delay(10)
 pygame.display.flip()
pygame.quit()
