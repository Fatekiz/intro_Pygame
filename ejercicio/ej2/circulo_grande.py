import pygame
import math

class Circulo_grande():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = (0,255,0)
        self.velocidad = 5

    def dibujar(self,ventana):
        center = (self.x,self.y)
        radio = 90
        pygame.draw.circle(ventana,self.color,center,radio)

    def mover(self, teclas):

        movimiento_x = 0
        movimiento_y = 0

        # Movimientos en el eje y 
        if teclas[pygame.K_UP]:
                movimiento_y = - self.velocidad
        if teclas[pygame.K_DOWN]:
            movimiento_y = self.velocidad
            
            # Movimientos en el eje x
        if teclas[pygame.K_RIGHT]:
            movimiento_x = self.velocidad
        if teclas[pygame.K_LEFT]:
            movimiento_x = - self.velocidad

            # Ajustando velocidad para cuando hayan movimientos en diagonales
        if movimiento_x != 0 and movimiento_y != 0:
            movimiento_x /= math.sqrt(2)
            movimiento_y /= math.sqrt(2)

            # actualizando los movimientos
        self.x += movimiento_x
        self.y += movimiento_y