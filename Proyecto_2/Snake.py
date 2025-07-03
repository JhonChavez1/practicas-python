import turtle
import time
import random

retraso = 0.1

s = turtle.Screen()
# s.setup(750, 750)               # Dar un tamaño a la pantalla
# s.bgcolor("gray")               # color de la pantalla
s.title("Snake")

snake = turtle.Turtle()
snake.speed(1)
snake.shape("square")
snake.penup()
snake.direction = "stop"        # snake.direction = define la dirección de la serpiente. "stop" Reinicia la serpiente a su lugar inicial cuando la toca una parte de la pantalla
snake.color("green")

comida = turtle.Turtle()
comida.shape("circle")
comida.color("Red")
comida.penup()
comida.goto(0, 100)

def arriba():
    snake.direction = "up"

def abajo():
    snake.direction = "down"

def derecha():
    snake.direction = "right"

def izquierda():
    snake.direction = "left"


# dirección de la serpiente
def movimiento():
    if snake.direction == "up":
        y = snake.ycor()        # devuelve la ubicación en el eje Y del objeto 
        snake.sety(y + 10)      # designando el movimiento hacia arriba
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 10)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 10)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 10)

s.listen()                      # poner a escuchar la pantalla
s.onkeypress(arriba, "Up")      # presionar la teclas del teclado
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")




# movimientos repetitivos
while True:
    s.update()

 # movimentos de la comida aleatoria   
    if snake.distance(comida) < 20:   # sistance = método el cual nos permite determinar la distancia de un objeto. "En este caso hacia comida"
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x, y)


    movimiento()
    time.sleep(retraso) 







turtle.done()