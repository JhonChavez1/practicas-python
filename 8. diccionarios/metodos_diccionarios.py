
diccionario = {1:2, 2:3, 3:4, 4:5}
print(diccionario)

diccionario2= {5:6, 6:7}

# eliminar una clave con su respectivo valor
# eliminar una clave 3
diccionario.pop(3)
print(diccionario)
# método para mostrar el valor de la llave 2 del diccionario 
diccionario.get(2) 
# método para agregar valores. Agrega al final del diccionario
diccionario.setdefault(5, 6)
print(diccionario)
# método para actualizar un diccionario con añadiendo otro dicicionario. Si hay una clave repetida entonces solo se va a mantener una
diccionario.update(diccionario2)
print(diccionario)
# generar una copia del diccionario
diccionario.copy()
print(diccionario)
# método para eliminar las claves y valores de un diccionario
diccionario.clear()
print(diccionario)