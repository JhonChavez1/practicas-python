import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.begin_fill()          # Iniciar rellenado
t.circle(100)           # todo el códidgo que esté dentro del begin y el end es el que se va a rellenar
t.end_fill()            # Finalizar rellenado

'''
t.begin_fill()
t.color("white") # color(circulo, tortuga)
t.circle(50)
t.end_fill()
'''
t.rt(100)
t.forward(100)
t.rt(100)
t.forward(100)

# modificar la tortuga
t.speed(1)
t.shape("turtle")       # Tortuga
t.lt(50)
t.fd(100)
t.shape("arrow")        # Flecha
t.rt(50)
t.fd(100)
t.shape("circle")       # Circulo
t.lt(50)
t.fd(100)
t.shape("square")       # Cuadrado  
t.rt(150)
t.fd(150)
t.shape("triangle")     # Triangulo
t.rt(100)
t.fd(100)
t.shape("classic")      # El que viene por defecto

t.penup()               # Levantar el lapíz
t.fd(100)
t.pendown()             # Dibujar nuevamente
t.fd(100)

t.undo()                # Es un retroceso a la última acción
t.clear()               # Limpiar toda la pantalla
t.reset()               # reiniciar el programa

t.forward(100)
t.stamp()               # Dejar una marca
t.forward(100)



turtle.done()