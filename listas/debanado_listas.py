
lista = [10, 20, 3.14, "Walter", "Coto", 7, "Estudiante", "Cuaderno"]

print(lista[5])
#debanado desde el campo 0 hasta el 5. recordar que no muestra el campo de la derecha
print(lista[0 : 5])
# debanado desde el campo 0 hasta el 5
print(lista[ : 5])
# mostrando desde el 1 hasta el último dato
print(lista[1: ])
# cuando hay un número negativo el conteo empieza desde el último hacia adelante
# mostrar el último dato
print(lista[-1])
# cuando hay dos negativos el mayor debe de estar a la izqierda y el menor a la derecha
# mostrar el dato 5 de atrás hacia adelante hata el campo 2 de atras hacia adelante
print(lista[-5 : -2])