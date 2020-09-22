import turtle
import gc
import time
import keyword
import random

tiempo= 0.0001
desplasamiento=4 
width=750
height=750
puntuacion=0
maximapuntuacion=0

# Configuracion de la ventana
win =turtle.Screen()
win.title("Snake 3D?")
win.bgcolor("black")
win.setup(width,height)
win.tracer(0)
alto=int(width/2)
ancho=int(height/2)
##########################Marcador

marcador= turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0,alto-50)
marcador.write("Puntuacion: {} Maxima Puntuacion: {}".format(puntuacion,maximapuntuacion),align="center",font=("Courier"))

#Cabeza serpiente
cabeza= turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"
cabeza.color("dark green")

#cuerpo de la serpiente

cuerpo=[]
# comida de la serpiente
comida= turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,100)
comida.color("red")
#Funciones---------------------------

#Define el movimiento de la serpiente
def mov():
    
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y+desplasamiento)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y-desplasamiento)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x-desplasamiento)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x+desplasamiento)

def arriba():
    if cabeza.direction != "down":
        cabeza.direction ="up"

def abajo():
    if cabeza.direction != "up":
        cabeza.direction ="down"

def izq():
    if cabeza.direction != "right":
        cabeza.direction ="left"

def der():
    if cabeza.direction != "left":
        cabeza.direction ="right"

        
#define el movimiento del cuerpo de la serpiente
def movCuerpo():
    totalSeg = len(cuerpo)
    for index in range(totalSeg -1, 0, -1):
        x = cuerpo[index - 1].xcor()
        y = cuerpo[index - 1].ycor()
        cuerpo[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x, y)
   
#cambia la direccion de la cabeza
win.listen()
win.onkeypress(arriba,"Up")
win.onkeypress(abajo,"Down")
win.onkeypress(izq,"Left")
win.onkeypress(der,"Right")

#####################################################################################

start=True
while start:
    win.update()
    movCuerpo()
    mov()
    if cabeza.distance(comida) <20:   
        x=random.randint(-alto + 20,alto -20)
        y=random.randint(-ancho +20,ancho -20)
        comida.goto(x,y)
        nuevo_segmento= turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")  
        nuevo_segmento.penup()
        nuevo_segmento.goto(0,0)
        nuevo_segmento.direction="None"
        nuevo_segmento.color("green")
        cuerpo.append(nuevo_segmento)
        puntuacion+=10
        marcador.clear()
        if puntuacion >maximapuntuacion:
           maximapuntuacion=puntuacion
        marcador.write("Puntuacion: {} Maxima Puntuacion: {}".format(puntuacion,maximapuntuacion),align="center",font=("Courier"))
    ################################## CHOQUE######################################3
    if cabeza.xcor() >ancho or cabeza.xcor()<- ancho or cabeza.ycor()>alto or cabeza.ycor()< -alto:
        cabeza.direction="None"
        puntuacion=0
        cabeza.goto(0,0)
        while len(cuerpo)!=0:   
            cuerpo.pop()
        marcador.clear()
        marcador.write("Puntuacion: {} Maxima Puntuacion: {}".format(puntuacion,maximapuntuacion),align="center",font=("Courier"))
       

    time.sleep(tiempo)