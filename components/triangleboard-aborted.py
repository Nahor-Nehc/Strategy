import math
import pygame

class hexagrid:
  def __init__(self, x, y, sideLength, trianglesPerSide):
    self.x = x
    self.y = y
    self.triangleSideLength = sideLength/trianglesPerSide
    self.length = sideLength
    self.trianglesPerSide = trianglesPerSide

    self.coords = [[] for i in range(0, 2*self.trianglesPerSide+1)]
    self.triangles = []
    
    self.arialCoords = []
    
    #for each horizontal line in the hexagons
    for i in range(0, 2*self.trianglesPerSide+1):
      #maths
      lsin30 =  self.length*0.5
      lsin60 = self.length*(math.sqrt(3)/2)
      lineLen = self.length + (self.length/self.trianglesPerSide)*(-1*abs(self.trianglesPerSide-i)+self.trianglesPerSide)
      x1 = self.x +lsin30*abs((self.trianglesPerSide-i)/self.trianglesPerSide)
      y1 = self.y + lsin60*i/self.trianglesPerSide
      x2 = x1 + lineLen
      y2 = y1
      
      #for each point of a triangle on the line
      for point in range(0, int(lineLen/self.triangleSideLength)+1):
        x = x1 + self.triangleSideLength*point
        y = y1
        self.coords[i].append((x, y))
        
    #the top row of triangles
    self.triangles.append([(self.coords[0][i], self.coords[0][i+1], self.coords[1][i+1]) for i in range(0, len(self.coords[0])-1)])
    
    #the rows between the top and middle rows
    for line in range(1, int(len(self.coords)/2)):
      self.triangles.append([(self.coords[line][i], self.coords[line][i+1], self.coords[line-1][i]) for i in range(0, len(self.coords[0])-1+line)])
      self.triangles.append([(self.coords[line][i], self.coords[line][i+1], self.coords[line+1][i+1]) for i in range(0, len(self.coords[0])-1+line)])
    
    #the middle rows
    line =  int(len(self.coords)/2)
    self.triangles.append([(self.coords[line][i], self.coords[line][i+1], self.coords[line-1][i]) for i in range(0, len(self.coords[0])-1+line)])
    self.triangles.append([(self.coords[line][i], self.coords[line][i+1], self.coords[line+1][i]) for i in range(0, len(self.coords[0])-1+line)])
    
    #the rows between the middle rows and last row
    for line in range(int(len(self.coords)/2+1), len(self.coords)-1):
      self.triangles.append([(self.coords[line][i], self.coords[line][i+1], self.coords[line-1][i+1]) for i in range(0, len(self.coords[0])+(2*self.trianglesPerSide-1)-line)])
      self.triangles.append([(self.coords[line][i], self.coords[line][i+1], self.coords[line+1][i]) for i in range(0, len(self.coords[0])+(2*self.trianglesPerSide-1)-line)])
      
    #the last row
    self.triangles.append([(self.coords[-1][i], self.coords[-1][i+1], self.coords[-2][i+1]) for i in range(0, len(self.coords[-1])-1)])
    
  def draw(self, window):
    for row in self.triangles:
      for triangle in row:
        pygame.draw.polygon(window, (0, 255, 0), triangle)
        pygame.draw.polygon(window, (0,0, 0), triangle, 1)