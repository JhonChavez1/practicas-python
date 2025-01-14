'''
Escribir un programa que pida un número al usuario y muestre las tablas de multiplicar de ese número
'''

numero = int(input("Por favor ingrese un número: "))
j = 0
i = 0

while i < 10:
    i += 1
    j += 1
    print(numero, "*", j, "=", i * numero)


# solución 2 empezando desde 0 y utilizando el método .format

numero1 = int(input("Por favor ingrese un número: "))
i = 0
multi = 0

while i <= 10:
    multi = numero1 * i
    print("{} x {} = {}".format(numero, i, multi))
    i += 1


