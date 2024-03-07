from random import choice
jugadores=["Ferran", "Sergio", "Esteban", "Roberto", "Sedeño", "Riker", "Ambro","Eladri"]

equipoA= []
equipoB= []

while len(jugadores) > 0:
    jugadorA=choice(jugadores)
    print(jugadorA)
    equipoA.append(jugadorA)
    jugadores.remove(jugadorA)
    print("Jugadores restantes: ",jugadores)

    jugadorB=choice(jugadores)
    print (jugadorB)
    equipoB.append(jugadorB)
    jugadores.remove(jugadorB)
    
    print("Equipo A: ", equipoA)
    print("Equipo B: ", equipoB)
    print()