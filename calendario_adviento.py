from tkinter import *
from math import *
ventana=Tk()
ventana.title("Calendario Adviento para Ferran")
ventana.geometry("900x500")

#TAMAÑO BOTONES
ancho_boton=15
alto_boton=4

#COLOR
ventana.configure(background="green")
color_boton=("red")

results=Label(ventana,text="")
results.config(fg="black",bg="green", font=("Arial",14))
results.place(x=200, y=440)

lista=["Vamos a jugar al lol juntos","Te invito al Toro Burger","Te invito a churros","Vamos a echarnos un warzone","Te vienes a mi casa y vemos una peli","Vamos a jugar al lol","Nos jugamos una botlane","Te invito a una cocacola","Te regalo una flor","Te invito a un café","Vamos al parque a comer pipas","Vamos a secuestrar a sergio","Te invito a comer","Vamos a jugar al monopoli","Te voy a regalar la nueva skin de ornn","Vamos al dominos","Vamos al indian","Te voy a regalar un huevo kinder","Vamos al TacoBell","Vamos a ver una peli navideña","Vamos a jugar al MW2","Te voy a regalar una pelota de basket","Vamos a ver las luces de navidad en Málaga","Vamos al airsoft","Te regalo el pase del LoL"]

def function(dia,label):
    label.config(text=lista[dia-1])
    

#CREAMOS VARIABLES PARA LOS BOTONES
Boton0=Button(ventana, text="Día 1", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(1,results)).place(x=20, y=20)
Boton1=Button(ventana, text="Día 2", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(2,results)).place(x=170, y=20)
Boton2=Button(ventana, text="Día 3", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(3,results)).place(x=320, y=20)
Boton3=Button(ventana, text="Día 4", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(4,results)).place(x=470, y=20)
Boton4=Button(ventana, text="Día 5", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(5,results)).place(x=620, y=20)
Boton5=Button(ventana, text="Día 6", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(6,results)).place(x=770, y=20)
Boton6=Button(ventana, text="Día 7", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(7,results)).place(x=20, y=120)
Boton7=Button(ventana, text="Día 8", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(8,results)).place(x=170, y=120)
Boton8=Button(ventana, text="Día 9", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(9,results)).place(x=320, y=120)
Boton0=Button(ventana, text="Día 10", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(10,results)).place(x=470, y=120)
Boton0=Button(ventana, text="Día 11", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(11,results)).place(x=620, y=120)
Boton0=Button(ventana, text="Día 12", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(12,results)).place(x=770, y=120)
Boton0=Button(ventana, text="Día 13", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(13,results)).place(x=20, y=220)
Boton0=Button(ventana, text="Día 14", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(14,results)).place(x=170, y=220)
Boton0=Button(ventana, text="Día 15", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(15,results)).place(x=320, y=220)
Boton0=Button(ventana, text="Día 16", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(16,results)).place(x=470, y=220)
Boton0=Button(ventana, text="Día 17", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(17,results)).place(x=620, y=220)
Boton0=Button(ventana, text="Día 18", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(18,results)).place(x=770, y=220)
Boton0=Button(ventana, text="Día 19", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(19,results)).place(x=20, y=320)
Boton0=Button(ventana, text="Día 20", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(20,results)).place(x=170, y=320)
Boton0=Button(ventana, text="Día 21", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(21,results)).place(x=320, y=320)
Boton0=Button(ventana, text="Día 22", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(22,results)).place(x=470, y=320)
Boton0=Button(ventana, text="Día 23", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(23,results)).place(x=620, y=320)
Boton0=Button(ventana, text="Día 24", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(24,results)).place(x=770, y=320)
Boton0=Button(ventana, text="Día 25", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:function(25,results)).place(x=20, y=420)



ventana.mainloop()