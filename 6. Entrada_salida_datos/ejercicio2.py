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
prom = (pp +2*ep + 3*ef) / 6

print("el promedio de practica de cada estudiante es :\n",pp)
print(("el promedio por cada alumno es: \n") , prom)
