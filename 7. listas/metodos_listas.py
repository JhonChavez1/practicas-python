
lista =[1, 2, 3, 4, 5]
print(lista)

# agregar mas datos a una lista
lista.append(6)
print(lista)

lista.append("Python")
print(lista)

# insertar un dato en un posición en especifica de la lista
# con el insert le podemos pasar dos parámetros, la posición y el valor
# agregar el dato 2.5 a la posición 2
lista.insert(2, 2.5)
print(lista)


lista1 = [1, 6, 2, 5, 3, 4, 5, 5]

# contar cuantos 5 hay en la lista
print(lista1.count(5))
# buscar un dato donde está el primer valor
print(lista.index(4)) 
# método para ordenar una lista de forma ascendente
lista1.sort()
print(lista)
# método para ordenar una lista de forma descendente
lista.reverse()
print(lista)


