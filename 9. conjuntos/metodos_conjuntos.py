
conjunto = {1, 1, 2, 3, 4, 5}
lista = [1, 1, 2, 3, 4, 5]

print(lista)
print(conjunto)

# como añadir un elemento
conjunto.add(20)
print(conjunto)
# eliminar un valor
conjunto.remove(1)
print(conjunto)
# discard cumple lo mismo que el remove
conjunto.discard(5)
print(conjunto)
# eliminar cualquier dato al azar
conjunto.pop()
print(conjunto)
# añadir elementos . Recuerde que no se puede añadir elementos repetidos
conjunto.update([6, 7, 9])
print(conjunto)
# eliminar todos los datos del conjunto
conjunto.clear()
print(conjunto)

