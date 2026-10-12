import math
import pygame

SIN30 = 0.5
SIN60 = math.sqrt(3)/2

class grid:
  def __init__(self, x, y, hex_length, row_number, col_number, type="rectangle"):
    
    cols = [lambda x, l: x, 
      lambda x, l: x + l*SIN30, 
      lambda x, l: x + l*SIN30 + l, 
      lambda x, l: x + l*SIN30*2 + l
      ]
    
    rows = [lambda y, l: y, 
      lambda y, l: y+l*SIN60, 
      lambda y, l: y+l*SIN60*2
      ]
    
    self.hex_coords = lambda x, y, l: [(cols[1](x, l), rows[0](y, l)), 
      (cols[2](x, l), rows[0](y, l)), 
      (cols[3](x, l), rows[1](y, l)), 
      (cols[2](x, l), rows[2](y, l)),
      (cols[1](x, l), rows[2](y, l)),
      (cols[0](x, l), rows[1](y, l))
      ]
    
    self.x = x
    self.y = y
    self.l = hex_length
    self.row_number = row_number
    self.col_number = col_number
    self.type = type
  
  def draw(self, window):
    
    if self.type == "rectangle":
      xs = [120*n+ self.x for n in range(0, math.ceil(self.col_number/2))]
      ys = [40*SIN60*2*n +self.y for n in range(0, self.row_number)]
      
      [[pygame.draw.polygon(window, (255, 255, 255), self.hex_coords(x, y, 40)) for x in xs] for y in ys]
      [[pygame.draw.polygon(window, (0, 0, 250), self.hex_coords(x, y, 40), 3) for x in xs] for y in ys]
      
      xs2 = [120*n+60 + self.x for n in range(0, math.floor(self.col_number/2))]
      ys2 = [40*SIN60*2*n+40*SIN60 +self.y for n in range(0, self.row_number)]
      
      [[pygame.draw.polygon(window, (255, 255, 255), self.hex_coords(x, y, 40)) for x in xs2] for y in ys2]
      [[pygame.draw.polygon(window, (0, 250, 0), self.hex_coords(x, y, 40), 3) for x in xs2] for y in ys2]