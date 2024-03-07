from tkinter import *
from math import *
ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600")

#TAMAÑO BOTONES
ancho_boton=11
alto_boton=3

#COLOR
ventana.configure(background="black")
color_boton=("SkyBlue2")

#DEFINIMOS EL VALOR DE LOS BOTONES
def btnClick(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador)


#CREAMOS FUNCION PARA EFECTUAR LA OPERACION
def operacion():
    global operador
    if "π" in operador:
        operador=operador.replace("π","3.14")
    try:
        opera=eval(operador)
    except:
        clear()
        opera=("ERROR")
    input_text.set(opera)

#FUNCION PARA LIMPIAR PANTALLA
def clear():
    global operador
    operador=("")
    input_text.set(operador)

#CREAMOS VARIABLES PARA LA FUNCION btnClick
    
input_text=StringVar()
operador=""


#CREAMOS VARIABLES PARA LOS BOTONES
Boton0=Button(ventana, text="0", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(0)).place(x=17, y=180)
Boton1=Button(ventana, text="1", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(1)).place(x=107, y=180)
Boton2=Button(ventana, text="2", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(2)).place(x=197, y=180)
Boton3=Button(ventana, text="3", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(3)).place(x=287, y=180)
Boton4=Button(ventana, text="4", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(4)).place(x=17, y=240)
Boton5=Button(ventana, text="5", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(5)).place(x=107, y=240)
Boton6=Button(ventana, text="6", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(6)).place(x=197, y=240)
Boton7=Button(ventana, text="7", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(7)).place(x=287, y=240)
Boton8=Button(ventana, text="8", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(8)).place(x=17, y=300)
Boton9=Button(ventana, text="9", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(9)).place(x=107, y=300)
Boton0=Button(ventana, text="π", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick("π")).place(x=197, y=300)
Boton0=Button(ventana, text=",", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(",")).place(x=287, y=300)
Boton0=Button(ventana, text="+", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick("+")).place(x=17, y=360)
Boton0=Button(ventana, text="-", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick("-")).place(x=107, y=360)
Boton0=Button(ventana, text="*", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick("*")).place(x=197, y=360)
Boton0=Button(ventana, text="/", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick("/")).place(x=287, y=360)
Boton0=Button(ventana, text="√", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick("√")).place(x=17, y=420)
Boton0=Button(ventana, text="(", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick("(")).place(x=107, y=480)
Boton0=Button(ventana, text=")", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick(")")).place(x=197, y=480)
Boton0=Button(ventana, text="=", width=ancho_boton, height=alto_boton,bg=color_boton,command=operacion).place(x=287, y=480)
Boton0=Button(ventana, text="ln", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick("ln")).place(x=17, y=480)
Boton0=Button(ventana, text="C", width=ancho_boton, height=alto_boton,bg=color_boton,command=clear).place(x=107, y=420)
Boton0=Button(ventana, text="EXP", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick("EXP")).place(x=197, y=420)
Boton0=Button(ventana, text="%", width=ancho_boton, height=alto_boton,bg=color_boton,command=lambda:btnClick("%")).place(x=287, y=420)



Salida=Entry(ventana,font=("arial",20,"bold"),width=22,bd=20,insertwidth=4,bg="powder blue", justify="right",textvariable=input_text).place(x=10, y=60)


ventana.mainloop()