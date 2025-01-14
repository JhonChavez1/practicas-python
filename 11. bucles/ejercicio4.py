'''
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares
'''

numero1 = int(input("Por favor ingresar un número: "))
numero2 = int(input("Por favor ingresar un número: "))

for i in range(numero1, numero2, 2):
    if i == numero2:
        break
    
    print(i)

# Respuesta correcta

num1 = int(input("Por favor ingrese el peirme número: "))
num2 = int(input("Por favor ingrese el segungo número: "))

for i in range(num1, num2, +1):
    # saltar los números pares
    if i % 2 == 0:
        continue
    print(i)