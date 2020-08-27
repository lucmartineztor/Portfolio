import random
import turtle
import time
import os

delay=0.1
score=0
Highscore=0
x1=int(input("ancho entre 400 y 900: "))
y1=int(input("altura entre 400 y 900: "))
pixel=20
segments=[]

#--------CREACION FRAME PRINCIPAL--------	
frame= turtle.Screen()
frame.title("snake game")
frame.bgcolor("yellow")
frame.setup(width=x1, height=y1)
frame.tracer(0)#turns off screen update

#------CREACION DE OBJETOS TIPO TORTUGA----------

#------ Culebra--------

head=turtle.Turtle() #Creacion objeto tipo tortuga
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()#elimina el rastro de la tortuga
head.goto(0,0)#posición inicial
head.dir="stop"


#---------Comida--------

food=turtle.Turtle()
food.speed(0)
shape=random.choice(["square","circle"])
color=random.choice(["red","blue","green"])
food.penup()
food.goto(0,100)


#-------- Tablero de puntuacion
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("grey")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Puntuación: {} Mayor puntuación:{}".format(score,Highscore), align="center", font=("Courier",24,"normal"))
#------------------



#--------------FUNCIONES---------------

#---------- Traslacion---------


def move():
	if head.dir=="up":
		y=head.ycor() #Aumento en la posicion en el eje y de un "pixel"
		head.sety(y+pixel)
	if head.dir=="down":
		y=head.ycor()
		head.sety(y-pixel)
	if head.dir=="left":
		x=head.xcor()
		head.setx(x-pixel)
	if head.dir=="right":
		x=head.xcor()
		head.setx(x+pixel)

#----------Cambio de dirección---------------

def go_up():
	if head.dir!="down":
		head.dir="up"
def go_down():
	if head.dir!="up":
		head.dir="down"
def go_left():
	if head.dir!="right":
		head.dir="left"
def go_right():
	if head.dir!="left":
		head.dir="right"

#--------------DEFINICION EVENTOS CON TRIGGER----
frame.listen()
frame.onkeypress(go_up,"w")
frame.onkeypress(go_down,"s")
frame.onkeypress(go_left,"a")
frame.onkeypress(go_right,"d")



#------------Coger la comida------



while True:
	frame.update()
	if head.distance(food)<pixel:
		x=random.randint(-x1/2+pixel,x1/2-pixel) #Genera una coordenada aleatoria
		y=random.randint(-y1/2+pixel,y1/2-pixel) # donde la comida se posiciona
		food.goto(x,y)

		new_segment=turtle.Turtle() #Generacion de objetos tipo turtle como extensión del cuerpo
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color("grey")
		new_segment.penup()
		segments.append(new_segment)
		delay -=0.01 #cambio de velocidad
		score += 10 #Puntuación

		if score >Highscore:
			Highscore=score

		pen.clear()
		pen.write("Score: {} High score:{}".format(score,Highscore), align="center", font=("Courier",24,"normal"))

	for index in range(len(segments)-1,0,-1):#indica que la posicion de un elemento ocupara la misma del anterior al moverse
		x=segments[index-1].xcor()
		y=segments[index-1].ycor()
		segments[index].goto(x,y)

	if len(segments)>0:#indica que la posicion de la cabeza es posicion cero en el arreglo
		x=head.xcor()
		y=head.ycor()
		segments[0].goto(x,y)

#--------Choque con la pared----------

	if head.xcor()>x1/2-pixel  or head.xcor()<-x1/2+pixel or head.ycor()>y1/2-pixel or head.ycor()<-x1/2+pixel:
		time.sleep(1)
		head.goto(0,0)
		head.dir="stop"
		score=0  #retoma valores iniales
		delay=0.1

		for segment in segments:
			segment.goto(x1+pixel,y1+pixel) #Saca de la vista los elementos de la partida anterior
		
		segments.clear()
		pen.clear()
		pen.write("Score: {} High score:{}".format(score,Highscore), align="center", font=("Courier",24,"normal"))

	move()

#--------Choque con su cuerpo----------	
	for segment in segments:
		if segment.distance(head)<pixel:
			time.sleep(1)
			head.goto(0,0)
			head.direc="stop"
			
			for segment in segments:
				segment.goto(x1+pixel,y1+pixel)
				score=0
				delay=0.1
			segments.clear()
			pen.clear()
			pen.write("Score: {} High score:{}".format(score,Highscore), align="center", font=("Courier",24,"normal"))


	time.sleep(delay)



wn.mainloop()



