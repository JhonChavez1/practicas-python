'''
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de números entre ambas cifras
'''

for i in range (1, 11):
    print(i)

numero1 = int(input("Por favor ingrese el primer número del 1 al 10: " ))
numero2 = int(input("Por favor ingrese el segundo número del 1 al 10: "))

for j in range(numero1, numero2 + 1):
    print(j)
    if j == numero2:
        break

# solucion mas acertada

for i in range(1, 11):
    print(i)

num1 = int(input("Por favor ingrese un número: "))
num2 = int(input("Por favor ingrese el segundo número: "))

for i in range(num1, num2 +1):
    print(i)


