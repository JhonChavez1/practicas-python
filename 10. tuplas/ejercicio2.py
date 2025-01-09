'''
Escribir una tupla que tenga las letras del alfabeto. Luego, debes pedir al usuario un número, 
el que haya ingresado, es la letra que debe imprimir el programa
'''

tupla = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

numero = int(input("Por favor ingreser un número: "))

if numero <= 26:
    print(tupla[numero-1])
else:
    print("Número incorrecto")

