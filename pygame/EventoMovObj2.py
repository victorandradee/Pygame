import pygame
pygame.init()
largura = 640
altura = 480
posicao_x = largura / 2
posicao_y = altura / 2
tamanho = 10
# Criando uma janela com o título "Movimentação de objetos"
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Movimentação de objetos")
AMARELO = (222, 191, 8)
janela.fill(AMARELO)
deve_continuar = True
# Loop do jogo
while deve_continuar:
 # Checando eventos que estão ocorrendo neste momento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False
        # Se uma tecla for pressionada
        if event.type == pygame.KEYDOWN:
        # Se a tecla for a seta para a esquerda
            if event.key == pygame.K_LEFT:
                posicao_x -= 10
            # Se a tecla for a seta para a direita
            if event.key == pygame.K_RIGHT:
                posicao_x += 10
            # Se a tecla for a seta para cima
            if event.key == pygame.K_UP:
                posicao_y -= 10
            # Se a tecla for a seta para baixo
            if event.key == pygame.K_DOWN:
                posicao_y += 10
    pygame.draw.rect(janela, (0, 0, 0), (posicao_x, posicao_y, tamanho, tamanho))
    pygame.display.flip()
pygame.quit()
