import turtle

s = turtle.Screen()
t = turtle.Turtle()


t.penup()
t.goto(-150, 200)
t.pendown()

# esto es un cuadrado
t.lt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

t.penup()
t.goto(0, 180)
t.pendown()

# automatizando un cuadrado
for i in range(4):
    t.lt(90)
    t.fd(100)

t.penup()
t.goto(150, 50)
t.pendown()

# Esto es una secuencia de circulos
t.circle(100)
t.circle(90)
t.circle(80)
t.circle(70)
t.circle(60)
t.circle(50)
t.circle(40)
t.circle(30)
t.circle(20)
t.circle(10)

t.penup()
t.goto(-150, 50)
t.pendown()

# Automatizando la secuencia de circulos
resultado = input("Qieres imprimir una figura: ")
if resultado == "SI":
    while i <= 110:
        t.circle(i)
        i += 10
else:
    print("Ok")

turtle.done()
