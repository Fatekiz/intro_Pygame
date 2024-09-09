import pygame
from class_triangulo import Triangulo
#         |                      |
# Nombre de archivo     nombre del archivo

pygame.init() # iniciando pygame
ventana = pygame.display.set_mode((800,600)) # Tamaño de ventana
pygame.display.set_caption("Triángulo móbil")
background_color = (0,0,0)
running = True

#Creando el objetos
triangulo = Triangulo(400,100)

# Bucle principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    teclas = pygame.key.get_pressed() # Llamando la funcion de pygame para asignar las teclas

    triangulo.movimiento(teclas) # para mover el triangulo
    
    ventana.fill(background_color) # Relleno con el formato RGB 

    triangulo.dibujar(ventana)

    pygame.display.flip() # Actualizo la pantalla

    pygame.time.delay(30)






pygame.quit()