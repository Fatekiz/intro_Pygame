# importamos libreria 
import pygame

# inicializacion de Pygame
pygame.init()
# Configuracion de la ventana
ventana = pygame.display.set_mode((800,600)) # Tamaño de la ventana
pygame.display.set_caption("Juego_benja") # Titulo de la ventana

# Color de fondo
background_color = (243, 53, 13)

# Bucle principal del juego
running = True
while running:
    # Evento para cerrar la ventana
    for event in pygame.event.get():  # Lista de eventos
        if event.type == pygame.QUIT:
            running = False

    # Rellenar el fondo
    ventana.fill(background_color)
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Retardo para limitar la velocidad del bucle
    pygame.time.delay(30)

# Finalizar Pygame
pygame.quit()