import pygame
import random

anchura=640
altura=480

#diferentes formas de definir colores
rojo=pygame.Color('Red')
cyan=pygame.Color('Cyan')
azul=pygame.Color(0,0,255)
verde=(0,255,0)
blanco=(255,255,255)
negro=(0,0,0)


#cargamos imagen fondo
fondo=pygame.image.load('img/midlane.png')
#cargamos imagen personaje
akali=pygame.image.load('img/true_damage2.png')
#cargamos imagen comida
bola=pygame.image.load('img/bola.png')

#definimos las medidas del objeto principal que se mueve en pantalla
ancho_rect=akali.get_size()[0]
alto_rect=akali.get_size()[1]
#y definimos su posicion inicial
x=anchura/2 - ancho_rect/2
#y=altura/2 - alto_rect/2
#redefinimos la altura para que akali no aparezca flotando
y=altura - alto_rect - 10

#Hacemos lo mismo para la bola
ancho_bola=bola.get_size()[0]
alto_bola=bola.get_size()[1]
#y definimos su posicion inicial
x_bola=random.randrange(0,anchura-ancho_bola)
y_bola=random.randrange(0,altura-alto_bola)

#definimos la velocidad de los objetos
vel=7
vel_bola_x=random.randrange(-5,5)
vel_bola_y=random.randrange(-5,5)

volumen_musica=0.5

puntos=0
pygame.font.init()
color_texto=pygame.color("black")
font=pygame.font.SysFont('Arial',28)


pygame.init()  #ponemos en marcha PyGame

clock = pygame.time.Clock() #defino reloj para ver fps

pantalla=pygame.display.set_mode((anchura,altura))
pygame.display.set_caption('Jueguecito cada vez menos tonto')

#cargar música
pygame.mixer.music.load('musica.wav')
#reproducir música (con el -1 reproduce el archivo en bucle)
pygame.mixer.music.play(-1)
#poner el volumen
pygame.mixer.music.set_volume(volumen_musica)


#muerte=pygame.mixer.Sound('musica.wav')


jugar=True

while jugar:
    #parte 1: Manejar eventos
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            jugar=False

        if evento.type==pygame.KEYDOWN:
            print('Tecla pulsada: ',evento.unicode)
            if evento.key==pygame.K_q or evento.key==pygame.K_ESCAPE:
                jugar=False
            elif evento.key==pygame.K_m and volumen_musica<1:
                volumen_musica+=0.1
                pygame.mixer.music.set_volume(volumen_musica)
            elif evento.key==pygame.K_n and volumen_musica>0:
                volumen_musica-=0.1
                pygame.mixer.music.set_volume(volumen_musica)

    #hacemos captura de todas las teclas pulsadas
    teclas_pulsadas=pygame.key.get_pressed()

    if teclas_pulsadas[pygame.K_LEFT] and x>vel:
       print('Nos movemos a la izquierda')
       #x=x-vel
       x-=vel #ambas expresiones hacen lo mismo
    if teclas_pulsadas[pygame.K_RIGHT] and x<anchura-ancho_rect:
       print('Nos movemos a la derecha')
       #x=x+vel
       x+=vel #ambas expresiones hacen lo mismo
    if teclas_pulsadas[pygame.K_UP] and y>vel:
       print('Nos movemos hacia arriba')
       #y=y-vel
       y-=vel #ambas expresiones hacen lo mismo
    if teclas_pulsadas[pygame.K_DOWN] and y<altura-alto_rect:
       print('Nos movemos hacia abajo')
       #y=y+vel
       y+=vel #ambas expresiones hacen lo mismo
    
    #actualizar bola
    x_bola+=vel_bola_x
    y_bola+=vel_bola_y
    
    if x_bola>anchura-ancho_bola or x_bola<0:
        vel_bola_x=-vel_bola_x

    if y_bola>altura-alto_bola or y_bola<0:
        vel_bola_y=-vel_bola_y
    if abs((x+ancho_bola/2)-(x_bola+ancho_bola/2))<ancho_bola/2 and abs((y+alto_bola/2)-(y_bola+alto_bola/2))<alto_bola/2:
        puntos+=1
        cuenta_atras=fps
        #pygame.mixer.Sound.play(muerte)
        
        x_bola=random.randrange(0,anchura-ancho_bola)
        y_bola=random.randrange(0,altura-alto_bola)
        


    #Parte 2: dibujar pantalla en copia oculta
    #pantalla.fill(verde)
    pantalla.blit(fondo,(0,0))

    if cuenta_atras>0:
        pantalla.blit(akali_muerta(x,y))
        cuenta_atras-=1
    else:
        pantalla.blit(akali,(x,y))
        pantalla.blit(bola,(x_bola,y_bola))
        
    pantalla.blit(akali,(x,y))
    pantalla.blit(bola,(x_bola,y_bola))


    #parámetros de render: texto, suavizado, color
    img_texto=font.render(f"Runtos: {puntos}",True,color_texto)
    pantalla.blit(img_texto,(20,20))
    #pygame.draw.rect(pantalla,blanco,(x,y,ancho_rect,alto_rect))
    
    #Parte 3: refrescar la pantalla con la copia
    pygame.display.flip()
    clock.tick(60) #fijo los FPS a 60

#print(f'{clock.get_fps():2.0f} fps') #imprimo en consola los FPS
print(clock.get_fps(),' fps')
pygame.quit()