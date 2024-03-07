import sys
import pygame 

pygame.init()

#Colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE= (0,255,0)
ROJO = (255,0,0)
AZUL = (0,0,255)



tamaño = (800,600)

ventana = pygame.display.set_mode(tamaño)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


for i in range(100,700,100):
    pygame.draw.rect(ventana, BLANCO, (x, 230, 50, 50))