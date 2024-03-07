print("Bienvenido a tu calculadora de ahorros")
tipo1=input("Centimos a euro dia uno")
dia1=int(input("¿Cuánto quieres ahorrar el primer día?: "))
tipo2=input("Centimos a euro cada dia")
dia2=int(input("¿Cuánto quieres ahorrar cada día?: "))

periodo=365
total=0

if tipo1=="centimos":
    total+=dia1
else:
    total+=(dia1*100)
print("El primer día tienes ahorrado {total} céntimos o {total/100} euros")
for i in range(periodo-1):
    if tipo2=="centimos":
        total+=(dia2*(i+1))
    else:
        total+=((dia2*100)*(i+1))
        print("El dia numero {i+2} tienes ahorrado {total} céntimos o {total/100} euros")
print()
print("En {periodo} días vas a ahorrar {total} centimos o {total/100} euros")



