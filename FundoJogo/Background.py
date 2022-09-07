from turtle import back
import pygame
from pygame.locals import *

#Victor Andrade 32168144

pygame.init()

x = 900
y = 500


fundo = "FundoJogo/background.jpg"
tubarao = "FundoJogo/tubarão.png"

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("BACKGROUND")


background = pygame.image.load(fundo).convert_alpha()
background = pygame.transform.scale(background, (x,y))

playerImg = pygame.image.load(tubarao).convert_alpha()
playerImg = pygame.transform.scale(playerImg, (200,200))
playerImg = pygame.transform.rotate(playerImg, -90)

pos_player_x = 200
pos_player_y = 300

JogoAtivo = True

while JogoAtivo:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            JogoAtivo = False
        

    screen.blit(background, (0,0))
    
    rel_x = x % background.get_rect().width
    screen.blit(background, (rel_x - background.get_rect().width, 0))
    if rel_x < 900:
        screen.blit(background, (rel_x, 0))

    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 1

    if tecla[pygame.K_DOWN] and pos_player_y < 400:
        pos_player_y += 1

    if tecla[pygame.K_LEFT] and pos_player_x > 1:
        pos_player_x -= 1

    if tecla[pygame.K_RIGHT] and pos_player_x < 700:
        pos_player_x += 1

    x -= 0.5

    screen.blit(playerImg, (pos_player_x, pos_player_y))

    pygame.display.update()


