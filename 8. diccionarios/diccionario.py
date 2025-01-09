
diccionario = {"usuario": "Jhon", "contraseña": 12345}
print(diccionario)

diccionario1 = {"Nombre": "Jhon", "apellido": "Chavez", "estatura": 1.72}
print(diccionario1)

# método para imprimir solo las claves del diccioranio
print(diccionario1.keys())
# método para mostrar solo los valores
print(diccionario1.values())
# imprimir el valor de una llave
print(diccionario1["estatura"])
# agregar una clave y un valor a un diccionario
diccionario1["peso"] = "58 kg"
print(diccionario1)
# modificar el valor de una clave
diccionario1["Nombre"] = "Fanor"
print(diccionario1)