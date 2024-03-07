from random import randint
print("¡Vamos a jugar a pikachu!")
print("Las reglas son las siguientes:")
print("Jugamos a piedra papel o tijeras y quien gane la primera ronda le pellizca la mejilla al otro, si le pellizca las 2 mejillas le puede dar una torta")
#PRIMERA RONDA
jugador= input("¿piedra (r), papel (p) o tijeras(t)?")
print("Pika por arriba, pika por abajo, pi ka chu")
if (jugador == "r"):
    print("O", end =" ")
elif (jugador == "p"):
    print("___", end =" ")
elif (jugador == "t"):
    print("8<", end =" ")

print('contra', end= " ")

elegido=randint(1,3)

if elegido ==1:
    ordenador="r"
    print ("O")
elif elegido ==2:
    ordenador="p"
    print("___")
else:
    ordenador="t"
    print("8<")

if (jugador==ordenador):
    print("Empate!!")
elif (jugador == "r" and ordenador == "t"):
    print("Te he ganado la primera ronda, te pellizco la primera mejilla!!")
elif (jugador == "r" and ordenador == "p"):
    print("Me has ganado la primera ronda, me tienes que pellizcar la mejilla!!")

elif(jugador == "p" and ordenador == "r"):
    print("Me has ganado la primera ronda, me tienes que pellizcar la mejilla!!!!")
elif (jugador =="p" and ordenador == "t"):
    print("Te he ganado la primera ronda, te pellizco la primera mejilla!!")
    
elif(jugador == "t" and ordenador == "r"):
    print("Me has ganado la primera ronda, me tienes que pellizcar la mejilla!!!!")
elif (jugador =="t" and ordenador == "p"):
    print("Te he ganado la primera ronda, te pellizco la primera mejilla!!")
    
#SEGUNDA RONDA
jugador= input("¿piedra (r), papel (p) o tijeras(t)?")
print("Pika por arriba, pika por abajo, pi ka chu")
if (jugador == "r"):
    print("O", end =" ")
elif (jugador == "p"):
    print("___", end =" ")
elif (jugador == "t"):
    print("8<", end =" ")

print('contra', end= " ")

elegido=randint(1,3)

if elegido ==1:
    ordenador="r"
    print ("O")
elif elegido ==2:
    ordenador="p"
    print("___")
else:
    ordenador="t"
    print("8<")

if (jugador==ordenador):
    print("Empate!!")
elif (jugador == "r" and ordenador == "t"):
    print("Te he ganado la primera ronda, te pellizco la primera mejilla!!")
elif (jugador == "r" and ordenador == "p"):
    print("Me has ganado la primera ronda, me tienes que pellizcar la mejilla!!")

elif(jugador == "p" and ordenador == "r"):
    print("Me has ganado la primera ronda, me tienes que pellizcar la mejilla!!!!")
elif (jugador =="p" and ordenador == "t"):
    print("Te he ganado la primera ronda, te pellizco la primera mejilla!!")
    
elif(jugador == "t" and ordenador == "r"):
    print("Me has ganado la primera ronda, me tienes que pellizcar la mejilla!!!!")
elif (jugador =="t" and ordenador == "p"):
    print("Te he ganado la primera ronda, te pellizco la primera mejilla!!")
