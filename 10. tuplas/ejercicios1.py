'''
Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado es el mes que debe mostrar en la tupla
'''
# primera solución descartada
tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

mes = int(input("Por favor ingrese un númreo del 1 al 12: "))

if mes == 1:
    print(tupla[0])
elif mes == 2:
    print(tupla[1])
elif mes == 3:
    print(tupla[2])
elif mes == 4:
    print(tupla[3])
elif mes == 5:
    print(tupla[4])
elif mes == 6:
    print(tupla[5])
elif mes == 7:
    print(tupla[6])
elif mes == 8:
    print(tupla[7])
elif mes == 9:
    print(tupla[8])
elif mes == 10:
    print(tupla[9])
elif mes == 11:
    print(tupla[10])
elif mes == 12:
    print(tupla[11])
else:
    print("Número incorrecto")

# otra solución mas eficaz 2

tupla1 = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

opcion_mes = int(input("Por favor ingrese un número del 1 al 12: "))
opcion_mes -= 1

print(tupla1[opcion_mes])


# otra solución 3

tupla2 = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

meses = int(input("Ingrese un número del 1 al 12: "))

print(tupla2[meses-1])