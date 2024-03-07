from random import choice
jugadores=[]
file=open("jugadores.txt", "r")
jugadores=file.read().splitlines()
print(jugadores)

equipoA= []
equipoB= []

while len(jugadores) > 0:
    jugadorA=choice(jugadores)
    print(jugadorA)
    equipoA.append(jugadorA)
    jugadores.remove(jugadorA)
    print("Jugadores restantes: ",jugadores)

    if jugadores == []:
        break

    jugadorB=choice(jugadores)
    print (jugadorB)
    equipoB.append(jugadorB)
    jugadores.remove(jugadorB)
    
    print("Equipo A: ", equipoA)
    print("Equipo B: ", equipoB)
    print()