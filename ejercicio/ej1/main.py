import pygame
from class_triangulo import Triangulo
from class_cuadrado import Cuadrado
from class_circulo import Circulo
#         |                   |
# Nombre de archivo     nombre del la clase o lo que quiera importar

pygame.init() # iniciando pygame
ventana = pygame.display.set_mode((800,600)) # Tamaño de ventana
pygame.display.set_caption("Triángulo móbil")
background_color = (0,0,0)
running = True

# Creando el Triangulo
triangulo = Triangulo(500,100)
# Cuadrado
cuadrado = Cuadrado(400,100)

# Círculo
circulo = Circulo(300,100)


# Bucle principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    teclas = pygame.key.get_pressed() # Llamando la funcion de pygame para asignar las teclas

    triangulo.movimiento(teclas) # para mover el triangulo
    cuadrado.movimiento(teclas)
    circulo.movimiento(teclas)
    
    ventana.fill(background_color) # Relleno con el formato RGB 

    triangulo.dibujar(ventana) # x1 
    circulo.dibujar(ventana)
    cuadrado.dibujar(ventana) # x2 Dibujo los polígonos

    pygame.display.flip() # Actualizo la pantalla

    pygame.time.delay(30) # fps






pygame.quit()