import math
import pygame

class Rectangulo_chico():
    def __init__(self,x,y,ancho,alto):
        self.x = x #movimientos en los ejes (x,y)
        self.y = y
        self.color = (0,0,255)
        self.velocidad = 1 # aumento para los pixeles
        self.ancho = ancho
        self.alto = alto
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    # Rectangulo
    def dibujar(self, ventana):

        pygame.draw.rect(ventana,self.color,self.rect)

# el movimiento para el rectangulo

    def movimiento(self,teclas):

        movimiento_x = 0
        movimiento_y = 0

        
        # Movimientos en el eje y 
        if teclas[pygame.K_w]:
            movimiento_y = - self.velocidad
        if teclas[pygame.K_s]:
            movimiento_y = self.velocidad
        
        # Movimientos en el eje x
        if teclas[pygame.K_d]:
            movimiento_x = self.velocidad
        if teclas[pygame.K_a]:
            movimiento_x = - self.velocidad

        # Ajustando velocidad para cuando hayan movimientos en diagonales
        if movimiento_x != 0 and movimiento_y != 0:
            movimiento_x /= math.sqrt(2)
            movimiento_y /= math.sqrt(2)

        # actualizando los movimientos
        self.x += movimiento_x
        self.y += movimiento_y
        self.rect.x = self.x
        self.rect.y = self.y
    
    def restablecer_posicion(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def obtener_posicion(self):
        return(self.rect.x, self.rect.y)
    
    def cambiar_color(self,color):
        self.color = color