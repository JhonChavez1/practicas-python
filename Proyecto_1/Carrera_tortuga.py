import turtle
import random

s = turtle.Screen()
s.title("Primer Proyecto")
# s.bgcolor("gray")

verde = turtle.Turtle()
azul = turtle.Turtle()

verde.hideturtle()
verde.shape("turtle")
verde.color("green", "green")
verde.shapesize(2, 2, 2)
verde.pensize(3)

azul.hideturtle()
azul.shape("turtle")
azul.color("blue", "blue")
azul.shapesize(2, 2, 2)
azul.pensize(3)


verde.penup()
verde.goto(300, 100)
verde.pendown()
verde.circle(50)
verde.penup()
verde.goto(-350, 150)
verde.showturtle()


azul.penup()
azul.goto(300, -100)
azul.pendown()
azul.circle(50)
azul.penup()
azul.goto(-350, -50)
azul.showturtle()

dado = [1,2,3,4,5,6]

for i in range(20):
    if verde.pos() >= (200, 350):
        print("La tortuga verde ha ganado")
    elif azul.pos() >= (200, -350):
        print("La tortuga azula ha ganado")
        break
    else:
        turno1 = input("Presiona la tecla enter para avanzar la tortuga azul. ")
        turno1 = random.choice(dado)
        print("Tu número es: ", turno1,"\nverde avanza: ", turno1 * 5)
        verde.pendown()
        verde.forward(10 * turno1)

        turno2 = input("Presiona la tecla enter para avanzar la tortuga azul. ")
        turno2 = random.choice(dado)
        print("Tu número es: ", turno2, "\n azul avanzas: ", turno2 * 5)
        azul.pendown()
        azul.forward(10 * turno2)





turtle.done()