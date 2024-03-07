#Tu eres el narrador, no la máquina tenlo en cuenta.
from random import randint
print("¡Vamos a jugar a pikachu!")
print("Las reglas son las siguientes:")
print("Jugamos a piedra papel o tijeras y quien gane la primera ronda le pellizca la mejilla al otro, si le pellizca las 2 mejillas le puede dar una torta")
print("")
#PRIMERA RONDA
contador_jugador=0
contador_ordenador=0

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
    contador_jugador+=1
    
elif (jugador == "r" and ordenador == "p"):
    print("Me has ganado la primera ronda, me tienes que pellizcar la mejilla!!")
    contador_ordenador+=1
    
elif(jugador == "p" and ordenador == "r"):
    print("Me has ganado la primera ronda, me tienes que pellizcar la mejilla!!")
    contador_ordenador+=1
    
elif (jugador =="p" and ordenador == "t"):
    print("Te he ganado la primera ronda, te pellizco la primera mejilla!!")
    contador_jugador+=1
    
elif(jugador == "t" and ordenador == "r"):
    print("Me has ganado la primera ronda, me tienes que pellizcar la mejilla!!")
    contador_ordenador+=1

elif (jugador =="t" and ordenador == "p"):
    print("Te he ganado la primera ronda, te pellizco la primera mejilla!!")
    contador_jugador+=1
print("¡Vamos ",contador_jugador, " a ", contador_ordenador," !")
print("")
    
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
    print("Te he ganado la segunda ronda, te pellizco la primera mejilla!!")
    contador_jugador+=1
    
elif (jugador == "r" and ordenador == "p"):
    print("Me has ganado la segunda ronda, me tienes que pellizcar la mejilla!!")
    contador_ordenador+=1
    
elif(jugador == "p" and ordenador == "r"):
    print("Me has ganado la segunda ronda, me tienes que pellizcar la mejilla!!")
    contador_ordenador+=1
    
elif (jugador =="p" and ordenador == "t"):
    print("Te he ganado la segunda ronda, te pellizco la primera mejilla!!")
    contador_jugador+=1
    
elif(jugador == "t" and ordenador == "r"):
    print("Me has ganado la segunda ronda, me tienes que pellizcar la mejilla!!")
    contador_ordenador+=1
elif (jugador =="t" and ordenador == "p"):
    print("Te he ganado la segunda ronda, te pellizco la primera mejilla!!")
    contador_jugador+=1
print("¡Vamos ",contador_jugador, " a ", contador_ordenador," !")
print("")

#TERCERA RONDA

if contador_jugador == 2:
    print("")
elif contador_ordenador == 2:
    print("")
else: 
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
        print("Te he ganado la tercera ronda, te pellizco la primera mejilla!!")
        contador_jugador+=1
        
    elif (jugador == "r" and ordenador == "p"):
        print("Me has ganado la tercera ronda, me tienes que pellizcar la mejilla!!")
        contador_ordenador+=1
        
    elif(jugador == "p" and ordenador == "r"):
        print("Me has ganado la tercera ronda, me tienes que pellizcar la mejilla!!")
        contador_ordenador+=1
        
    elif (jugador =="p" and ordenador == "t"):
        print("Te he ganado la tercera ronda, te pellizco la primera mejilla!!")
        contador_jugador+=1
        
    elif(jugador == "t" and ordenador == "r"):
        print("Me has ganado la tercera ronda, me tienes que pellizcar la mejilla!!")
        contador_ordenador+=1

    elif (jugador =="t" and ordenador == "p"):
        print("Te he ganado la tercera ronda, te pellizco la primera mejilla!!")
        contador_jugador+=1
    print("¡Vamos ",contador_jugador, " a ", contador_ordenador," !")
    
if contador_ordenador > contador_jugador:
    print("")
    print("¡Me has ganado, me debes una torta!")
elif contador_ordenador < contador_jugador:
    print("")
    print("¡He ganado, preparate para la torta!")
else:
    print("")
    print ("¡Hemos empatado, te salvas por hoy de la torta!")