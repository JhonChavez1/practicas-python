import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.speed(5)          # darle velocidad (entre uno y 10)
t.circle(20)        # Hacer circulos (radio)
t.circle(100) 
t.dot(15)           # circulo relleno
t.hideturtle()      # Desaparecer la tortuga
t.circle(50)
t.setx(100)         # moviendo la tortuga hacia el eje X manteniendo el eje Y
t.sety(-100)        # moviendo la tortuga hacia el eje Y manteniendo el eje X



turtle.done()