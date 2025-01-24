'''
Escribir una función que reciba una muestra de números en una lista y devuelva su medida.
'''

def medida(*tupla):
    print(len(tupla))

medida(1, 2, 3, 4,)

# solución 2

def medida2(*tupla):
    return len(tupla)

print(medida2(1, 2, 3, 4, 5))