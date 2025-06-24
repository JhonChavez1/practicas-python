import turtle

s = turtle.Screen() # crear pantalla
# objeto + módulo + clase
t = turtle.Turtle() # pluma
 
# movimientos de la pluma
''''
t.backward(100) # atras
t.right(90)     # derecha
t.forward(100)  # adelante   
t.left(90)      # izquierda
t.forward(100)  # adelante 
'''
# forma corta
'''
t.bk(100)   # atrás
t.rt(90)    # derecha
t.fd(100)   # adelante
t.lt(90)    # izquierda
t.fd(100)   # adelante
'''
t.goto(100,100) # indicar la dirección a un punto específico
t.goto(-100,100)  
t.home()         # regresar al punto inicial, es decir a el centro del lienzo 
t.bk(100)   # atrás
t.rt(90)    # derecha
t.fd(100)   # adelante
t.lt(90)    # izquierda
t.fd(100)   # adelante
t.lt(90)
t.fd(100)

turtle.done() # para que la pantalla se quede fija
