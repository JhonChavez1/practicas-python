import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor("red")        # Color al lienzo
s.title("Proyecto 1")   # Modificar el nombre del lienzo

t.shapesize(10, 5, 1)   # Ajustar el tamaño (ancho, largo, borde)

t.fillcolor("white")    #Cambiar el color de la tortuga
t.forward(180)
t.pencolor("black")     # Cambiar el color de la tinta
t.forward(180)

t.color("green")        # Color de la tortuga
t.right(90)
t.forward(180)

t.pensize(5)            # Cambiar el grosor de la linea
t.forward(180)

turtle.done()