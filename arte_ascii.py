from random import randint
jugador= input("¿piedra (r), papel (p) o tijeras(t)?")

if (jugador == "r"):
    print("O", end =" ")
elif (jugador == "p"):
    print("___", end =" ")
elif (jugador == "t"):
    print("8<", end =" ")
#print(jugador, "contra", end=" ")

print('contra', end= " ")

elegido=randint(1,3)
#print(elegido)
if elegido ==1:
    ordenador="r"
    print ("O")
elif elegido ==2:
    ordenador="p"
    print("___")
else:
    ordenador="t"
    print("8<")
#print(ordenador)

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
    

    
