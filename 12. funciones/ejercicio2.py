'''
Escribir una función que reciba un número entero y devuelva su factorial
'''

import math


def funcion():
    numero = int(input("Por favor ingrese un número entero: "))
    factorial = math.factorial(numero)
    print(factorial)

funcion()

# otra forma de resolver

def factorial():
    num = int(input("Por favor ingrese un número enteroy positivo: "))
    if num > 0:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print(factorial)
    else:
        print("El número es negativo ")

factorial()

    