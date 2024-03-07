import pygame

pygame.init()
 
anchura=700
altura=700

rojo=(255,0,0)
verde=(0,255,0)
blanco=(255,255,255)
negro=(0,0,0)

#fuente=pygame.font.SysFont('arial',20)
#textos=fuente.render("Cuadrados", rojo)

coche_w=pygame.image.load('img/coche_w.png')
coche_d=pygame.image.load('img/coche_d.png')
coche_s=pygame.image.load('img/coche_s.png')
coche_a=pygame.image.load('img/coche_a.png')
fondo=pygame.image.load('img/carretera.png')
poli_a=pygame.image.load('img/poli_a.png')
poli_d=pygame.image.load('img/poli_d.png')
direccion="arriba"

def coche(superficie, x, y, ancho, alto):
    pantalla.blit(poli_d,(poli_pos_x,poli_pos_y, 50, 50))
    #pygame.draw.rect(superficie, VERDE, (x, y, ancho, alto))

def poli(superficie, x, y, ancho, alto):
    pantalla.blit(poli_a,(pos_x2,pos_y2, 50, 50))
    #pygame.draw.rect(superficie, NARANJA, (x, y, ancho, alto))


#ancho_rect=coche.get_size()[0]
#alto_rect=coche.get_size()[1]


#ancho_rect2=minion.get_size()[0]
#alto_rect2=minion.get_size()[1]


#x=anchura/2 - ancho_rect/2
#y=altura/2 - alto_rect/2
#vel=5

pr_x = 100
pr_y = 100
vr_x = 5
vr_y = 5

pn_x = 293
pn_y = 290
vn_x = 0
vn_y = 0


pos_x=-50
pos_y=50
vel_x=8


pos_x2=700
pos_y2=550
vel_x2=8




poli_ancho = 60
poli_alto = 60
poli_pos_x = 100
poli_pos_y = 100
poli_vel_x = 3

coche_ancho = 60
coche_alto = 60
coche_pos_x = 293
coche_pos_y = 270
coche_vel_x = 0
coche_vel_y = 0





pygame.init()

pantalla=pygame.display.set_mode((anchura,altura))
pygame.display.set_caption("Buggati en acción")
reloj=pygame.time.Clock()

jugar=True

while jugar:

    reloj.tick(60)

    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            jugar=False
        if evento.type==pygame.KEYDOWN:
            if evento.key==pygame.K_LEFT:
                direccion="izquierda"
                #print("Tecla pulsada: ", evento.unicode)
                vn_x=-10
            if evento.key==pygame.K_RIGHT:
                direccion="derecha"
                #print("Nos movemos a la derecha")
                vn_x=10
            if evento.key==pygame.K_DOWN:
                direccion="abajo"
                #print("Nos movemos hacia abajo")
                vn_y=10
            if evento.key==pygame.K_UP:
                direccion="arriba"
                #print("Nos movemos hacia arriba")
                vn_y=-10
            if evento.key==pygame.K_q:
                jugar=False

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                vn_x = 0
            if evento.key == pygame.K_LEFT:
                vn_x = 0
            if evento.key == pygame.K_DOWN:
                vn_y = 0
            if evento.key == pygame.K_UP:
                vn_y = 0

    poli_pos_x=poli_pos_x+vel_x
    if poli_pos_x>anchura:
        poli_pos_x=-230

    pos_x2=pos_x2-vel_x2
    if pos_x2<-230:
        pos_x2=700

    coche_pos_x +=vn_x
    coche_pos_y +=vn_y
    

    if poli_pos_x + poli_ancho > coche_pos_x and \
       poli_pos_x < coche_pos_x + coche_ancho and \
       poli_pos_y + poli_alto > coche_pos_y and \
       poli_pos_y < coche_pos_y + coche_alto:
        pygame.time.delay(1000)
        poli_pos_x = 100
        poli_pos_y = 100
        coche_pos_x = 293
        coche_pos_y = 270



    pantalla.blit(fondo,(0,0))
    pantalla.blit(poli_d,(poli_pos_x,poli_pos_y, 220, 220))
    pantalla.blit(poli_a,(pos_x2,pos_y2, 220, 220))
    
    #pantalla.blit(textos,(10,10))
    #pantalla.blit(coche_w,(pn_x,pn_y))
    
    #pygame.draw.rect(pantalla,verde, (pos_x,pos_y, 50, 50))
    #pygame.draw.rect(pantalla,rojo,(pos_x2,pos_y2, 50, 50))

    if direccion == "arriba":
        pantalla.blit(coche_w,(coche_pos_x,coche_pos_y))
    if direccion == "derecha":
        pantalla.blit(coche_d,(coche_pos_x,coche_pos_y))
    if direccion == "abajo":
        pantalla.blit(coche_s,(coche_pos_x,coche_pos_y))
    if direccion == "izquierda":
        pantalla.blit(coche_a,(coche_pos_x,coche_pos_y))


    #pygame.display.flip()
    pygame.display.update()
    

print(reloj.get_fps(),"fps")
pygame.quit()


#https://www.befunky.com/es/crear/editor-de-fotos/