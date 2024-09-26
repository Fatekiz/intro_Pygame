import pygame
import math

from circulo_chico import Circulo_chico
from circulo_grande import Circulo_grande

# iniciando pygame
pygame.init()
ventana = pygame.display.set_mode((1000,800))
background_color = (0,0,0)
# instanciar
circulito = Circulo_chico(100,100)
circulote = Circulo_grande(200,200)

def verificar_colision(circulo1, radio1, circulo2, radio2):
    distancia = math.sqrt((circulo2.x - circulo1.x)**2 + (circulo2.y - circulo1.y)**2)
    return distancia <= (radio1 + radio2)
# Bucle principal 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.key.get_pressed()
    # movimiento
    circulito.mover(teclas)
    circulote.mover(teclas)

    ventana.fill(background_color)
    circulito.dibujar(ventana)
    circulote.dibujar(ventana)
    
    # verificar que los triangulos se tocan
    if verificar_colision(circulito,50,circulote, 90):
        circulito.color = (255,0,0)
        circulote.color = (255,0,0)
    else:
        circulito.color = (0,0,255)
        circulote.color = (0,255,0)
        
    
    pygame.display.update() # 
pygame.quit()