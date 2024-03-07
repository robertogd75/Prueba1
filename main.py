import tkinter

#----- Ventana ---------

ventana=tkinter.Tk()
ventana.title("Calculadora de propinas")
ventana.geometry("800x700")
ventana.resizable(0,0)


#----- Etiqueta ---------

cabecera=tkinter.Label(ventana, text="Calculadora de Propinas", font=(20)).pack()


#----- Botones ---------


def salir():
    ventana.destroy()




boton_salir = tkinter.Button(ventana, text="Cerrar", command=salir, fg="red", font=(15))
boton_salir.pack()
boton_salir.place(x=665, y=600, height=80, width=100)


boton1 = tkinter.Button(ventana, text="1", font=(15))
boton1.pack()
boton1.place(x=50, y=240, height=80, width=100)


boton2 = tkinter.Button(ventana, text="2", font=(15))
boton2.pack()
boton2.place(x=200, y=240, height=80, width=100)


boton3 = tkinter.Button(ventana, text="3", font=(15))
boton3.pack()
boton3.place(x=350, y=240, height=80, width=100)


boton4 = tkinter.Button(ventana, text="4", font=(15))
boton4.pack()
boton4.place(x=50, y=360, height=80, width=100)


boton5 = tkinter.Button(ventana, text="5", font=(15))
boton5.pack()
boton5.place(x=200, y=360, height=80, width=100)


boton6 = tkinter.Button(ventana, text="6", font=(15))
boton6.pack()
boton6.place(x=350, y=360, height=80, width=100)


boton7 = tkinter.Button(ventana, text="7", font=(15))
boton7.pack()
boton7.place(x=50, y=480, height=80, width=100)


boton8 = tkinter.Button(ventana, text="8", font=(15))
boton8.pack()
boton8.place(x=200, y=480, height=80, width=100)


boton9 = tkinter.Button(ventana, text="9", font=(15))
boton9.pack()
boton9.place(x=350, y=480, height=80, width=100)


boton0 = tkinter.Button(ventana, text="0", font=(15))
boton0.pack()
boton0.place(x=200, y=600, height=80, width=100)

botonC = tkinter.Button(ventana, text="C", font=(15))
botonC.pack()
botonC.place(x=50, y=600, height=80, width=100)

botonB = tkinter.Button(ventana, text="Borrar", font=(15))
botonB.pack()
botonB.place(x=350, y=600, height=80, width=100)



ventana.mainloop()

