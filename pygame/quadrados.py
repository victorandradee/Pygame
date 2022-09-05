import pygame
import random 

pygame.init()
width = 600
height = 600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("EXERCICIO QUADRADOS")
BRANCO = (255, 255, 255)

screen.fill(BRANCO)

class Quadrado: 

    def __init__(self):
        self.altura = 0
        self.largura = 0
        self.cor = (0, 0, 0)
        self.posx = 0
        self.posy = 0

    def sorteiacor(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb = (r,g,b)
        self.cor= rgb
        return rgb

    def sorteiax(self):
        posx = random.randint(0, 600)
        while (posx + j > height):
            posx = random.randint(0,600)
        posx = int(posx)
        return posx


    def sorteiay(self):
        posy = random.randint(0, 600)
        while (posy + j > height):
            posy = random.randint(0,600)
        posy = int(posy)
        return posy



def main():
    q1 = Quadrado()
    global j
    j = 250
    
    while j !=0:
        pygame.draw.rect(screen, q1.sorteiacor(),(q1.sorteiax(), q1.sorteiay(), j, j), 0) 
        j = j/2
    





  
main()


pygame.display.flip()
pygame.time.delay(5000)
pygame.quit
