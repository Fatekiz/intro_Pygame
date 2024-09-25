import pygame
from class_rectangulo_chico import Rectangulo_chico
from class_rectangulo_grande import Rectangulo_grande
#         |                   |
# Nombre de archivo     nombre del la clase o lo que quiera importar

pygame.init() # iniciando pygame
ventana = pygame.display.set_mode((800,600)) # Tamaño de ventana
pygame.display.set_caption("Colisiones")
background_color = (0,0,0)
color_colision = (255,0,0)


# Creando el Triangulo
rectangulo_chico = Rectangulo_chico(200,200,100,50)
rectangulo_grande = Rectangulo_grande(400,300,150,100)


# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    teclas = pygame.key.get_pressed() # funcion para la funcionalida de las teclas

    # Almacenar la posicion
    pos_anterior_chico = rectangulo_chico.obtener_posicion()
    pos_anterior_grande = rectangulo_grande.obtener_posicion()

    rectangulo_chico.movimiento(teclas) # para mover el rectangulo
    rectangulo_grande.movimiento(teclas)

   # verificar colision rectangular
    if rectangulo_chico.rect.colliderect(rectangulo_grande.rect):
        rectangulo_chico.restablecer_posicion(*pos_anterior_chico)
        rectangulo_grande.restablecer_posicion(*pos_anterior_grande)
        rectangulo_chico.cambiar_color(color_colision)
        rectangulo_grande.cambiar_color(color_colision)
    else:
        rectangulo_chico.cambiar_color((0,0,255))
        rectangulo_grande.cambiar_color((0,255,0))
   
    
   
    ventana.fill(background_color) # Relleno con el formato RGB 

    rectangulo_chico.dibujar(ventana) 
    rectangulo_grande.dibujar(ventana)
  

    pygame.display.update()

pygame.quit()