'''Realizar un programa que haga el proceso de formula general  para la resolución de ecuaciones, sabiendo que la formula
general es la que está en la imagen, el usuario debe ingresar los valores de "a, b y c, y el programa debe hacer el proceso  
para que al final muestre el mensaje: "La solución es: <solucion> '''

from math import sqrt
#ejemplo: imprime la raiz cuadrada de 100
print(sqrt(100))

a = int(input("ingrese el valor de a: "))
b = int(input("ingrese el valor de b: "))
c = int(input("ingrese el valor de c: "))
x1 = 0
x2 = 0

if ((b**2)- (4*a*c)) < 0:
    print("No se puede realizar porque no se puede sacar raiz a un número negativo")
else: 
    x1 = (-b + sqrt((b**2)-(4*a*c)))/ (2*a)
    x2 = (-b -sqrt((b**2)-(4*a*c)))/(2*a)

    print("la solución es: \nx1=", x1, "\nx2=" ,x2)

# ((-b + b)**2) - (4 + a + c) / 2 + a
#print("la solucion es: " , X)

'''Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno de un determinado curso
conociendo las notas de: tres práctica, el examen parcial y el examen final.
considere: 
PP = (P1 + P2 + P3) / 3 PROM = (PP + 2*EP + 3*EF)/6
donde: PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final'''

p1 = float(input("ingrese el resultado de la primera practica: "))
p2 = float(input("ingrese el resultado de la segunda practica: "))
p3 = float(input("ingrese el resultado de la tercera practica: "))
ep = float(input("ingrese la nota del examen parcial: "))
ef = float(input("ingrese la nota del examen final: "))
pp = (p1 + p2 + p3) / 3
prom = pp +(2*ep) + ((3*ef) / 6)

print(("el promedio por cada alumno es: ") , prom)
