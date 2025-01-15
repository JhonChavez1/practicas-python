'''
Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; 
si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0
'''

def funcion():
    num1 = int(input("Por favor ingrese el primer número: "))
    num2 = int(input("Por favor ingrese el segundo número: "))
    if num1 > num2:
        return 1
    elif num1 == num2:
        return 0
    else:
        return -1
    
print(funcion())