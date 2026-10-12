import pygame
import sys

import components.board as board

pygame.init()

FPS = 30

WIDTH, HEIGHT = 700, 700

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("strategy")

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED =   (211,   0,   0)
GREEN = (  0, 150,   0)
DGREEN = ( 0, 100,   0)
BLUE =  (  0,   0, 211)
LBLUE = (137, 207, 240)
GREY =  (201, 201, 201)
LGREY = (231, 231, 231)
LBROWN  = (185, 122, 87)
DBROWN = (159, 100, 64)

def draw(bd):
  bd.draw(WIN)
  pygame.display.flip()


def main():
  
  bd = board.grid(10, 10, 40, 6, 9)
  
  #initiates the clock
  clock = pygame.time.Clock()

  #initiates game loop
  run = True
  while run:

    #ticks the clock
    clock.tick(FPS)

    #gets mouse position
    mouse = pygame.mouse.get_pos()

    #for everything that the user has inputted ...
    for event in pygame.event.get():

      #if the "x" button is pressed ...
      if event.type == pygame.QUIT:

        #ends game loop
        run = False

        #terminates pygame
        pygame.quit()

        #terminates system
        sys.exit()
        
    draw(bd)
  
  
main()