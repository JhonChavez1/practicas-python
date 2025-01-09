
# modificar datos de una lista

lista = ["Python", 24, "Rene", "alexander", 12]

# modificar el dato de la posición 3
lista[3] = "Alexander"
print(lista)
# mostra el dato de la posición 3
print(lista[3])


# eliminar datos de una lista
lista1 = ["Python", 24, "Rene", "alexander", 12]

# eliminar el último dato
lista.pop()
print(lista)
# eliminar un valor que deseamos de la lista dandole un paramétro al método
lista.remove("Python")
print(lista)