import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

s = turtle.Screen()
# s.setup(750, 750)               # Dar un tamaño a la pantalla
# s.bgcolor("gray")               # color de la pantalla
s.title("Snake")
s.tracer()

snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"        # snake.direction = define la dirección de la serpiente. "stop" Reinicia la serpiente a su lugar inicial cuando la toca una parte de la pantalla
snake.color("green")

comida = turtle.Turtle()
comida.shape("circle")
comida.color("Red")
comida.penup()
comida.goto(0, 100)
comida.speed(0)

cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup()
texto.hideturtle()
texto.goto(0, -250)
texto.write(f"Marcador: {marcador}\tMarcador más alto:  {marcador_alto}", align="center", font=("arial", 24))

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
        snake.sety(y + 20)      # designando el movimiento hacia arriba
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

s.listen()                      # poner a escuchar la pantalla
s.onkeypress(arriba, "Up")      # presionar la teclas del teclado
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")


# movimientos repetitivos
while True:
    s.update()

    if snake.xcor() > 350 or snake.xcor() < -350 or snake.ycor() > 300 or snake.ycor() < -250:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        snake.home()
        snake.direction = "stop"
        cuerpo.clear()

        marcador = 0
        texto.clear()
        texto.write(f"Marcador:   {marcador}\tMarcador más alto: {marcador_alto}", align="center", font=("arial", 24))



 # movimentos de la comida aleatoria   
    if snake.distance(comida) < 20:   # distance = método el cual nos permite determinar la distancia de un objeto. "En este caso hacia comida"
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        comida.goto(x, y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0, 0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador
        texto.clear()
        texto.write(f"Marcador:  {marcador}\tMarcador más alto: {marcador_alto}", align= "center", font = ("arial", 24))



        
    total = len(cuerpo)         # obtiene la longitud (es decir, la cantidad de elementos) de una colección como una lista, cadena, tupla,
    for index in range(total -1, 0, -1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x,y)

    if total >0:
        x = snake.xcor()
        y = snake.ycor()
        cuerpo[0].goto(x,y)

    movimiento()

    for i in cuerpo:
        if i.distance(snake) <20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            snake.home()
            cuerpo.clear()
            snake.direction = "stop"
    

    time.sleep(retraso) 







turtle.done()