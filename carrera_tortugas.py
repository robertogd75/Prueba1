from turtle import *
from random import randint

speed(50)
penup()
goto(-140, 140)

for paso in range(10):
    write(paso, align= "center")
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color("red")
ada.shape("turtle")

ada.penup()
ada.goto(-160, 100)
ada.pendown()



pepe=Turtle()
pepe.color("blue")
pepe.shape("turtle")

pepe.penup()
pepe.goto(-160,70)
pepe.pendown()



ferran=Turtle()
ferran.color("purple")
ferran.shape("turtle")

ferran.penup()
ferran.goto(-160,40)
ferran.pendown()

paco=Turtle()
paco.color("black")
paco.shape("turtle")

paco.penup()
paco.goto(-160,10)
paco.pendown()

for turno in range(70):
    ada.forward(randint(1,5))
    ferran.forward(randint(1,5))
    pepe.forward(randint(1,5))
    paco.forward(randint(1,5))
