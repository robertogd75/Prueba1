import pygame
 
anchura=640
altura=480

#rojo=pygame.Color("Red")
#cyan=pygame.Color("Cyan")
#azul=pygame.Color(0,0,255)
verde=(0,255,0)
blanco=(255,255,255)
negro=(0,0,0)

ancho_rect=20
alto_rect=20

x=anchura/2 - ancho_rect/2
y=altura/2 - alto_rect/2


vel=10

pygame.init()

pantalla=pygame.display.set_mode((anchura,altura))
pygame.display.set_caption("Juego")

jugar=True

while jugar:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            jugar=False
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_LEFT:
                print("Tecla pulsada: ", evento.unicode)
                x-=vel
            if evento.key==pygame.K_RIGHT:
                print("Nos movemos a la derecha")
                x+=vel
            if evento.key==pygame.K_DOWN:
                print("Nos movemos hacia abajo")
                y+=vel
            if evento.key==pygame.K_UP:
                print("Nos movemos hacia arriba")
                y-=vel
            if evento.key==pygame.K_q:
                jugar=False


    pantalla.fill(verde)
    pygame.draw.rect(pantalla,blanco,(x,y,ancho_rect,alto_rect))

    pygame.display.flip()

pygame.quit()