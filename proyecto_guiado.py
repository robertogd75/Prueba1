from random import randint
jugador= input("¿piedra (r), papel (p) o tijeras(t)?")
print(jugador, "contra", end=" ")
elegido=randint(1,3)
#print(elegido)
if elegido ==1:
    ordenador="r"
elif elegido ==2:
    ordenador="p"
else:
    ordenador="t"
print(ordenador)

if (jugador==ordenador):
    print("Empate!!")
elif (jugador == "r" and ordenador == "t"):
    print("El jugador ha ganado!!")
elif (jugador == "r" and ordenador == "p"):
    print("El ordenador ha ganado!!")

elif(jugador == "p" and ordenador == "r"):
    print("El ordenador ha ganado!!")
elif (jugador =="p" and ordenador == "t"):
    print("El jugador ha ganado!!")
    
elif(jugador == "t" and ordenador == "r"):
    print("El ordenador ha ganado!!")
elif (jugador =="t" and ordenador == "p"):
    print("El jugador ha ganado!!")
    

    
