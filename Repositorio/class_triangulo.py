import pygame

class Triangulo():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = (219,148,255) # Colo RGB
        self.velocidad = (5) # Velocidad en medida "Pixeles"
    

    
    def dibujar(self, ventana):
        puntos = [(self.x, self.y), (self.x - 50, self.y +100), (self.x + 50, self.y + 100)]
        pygame.draw.polygon(ventana,self.color, puntos)

    def movimiento(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.y += self.velocidad