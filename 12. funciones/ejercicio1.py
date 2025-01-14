'''
Crear un programa que tenga una lista, luego crear una función con la cual se van a pedir números al usuario para agregar a la lista. 
Debes crear una segunda funcion en donde se ordenen los números pares e impares dentro de dos listas nuevas
'''

lista = []


def numeros():
    i = 0
    while i <10:
        num = int(input("Por favor ingrese un número: "))
        lista.append(num)
        i += 1

def ordenar():
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print(pares)
    print(impares)

numeros()
ordenar()






    



