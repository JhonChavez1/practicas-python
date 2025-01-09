
'''
En el siguiente diccionario se encuentran capitales de los paises en el mundo, 
debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, 
en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras",
"Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", 
"Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
'''
# Mi solución

diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Tegucigalpa",
"Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", 
"Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Por favor ingrese el nombre de un país: ")

if pais == "Guatemala":
    print(diccionario.get("Guatemala"))
elif pais == "El salvador":
    print(diccionario.get("El Salvador"))
elif pais == "Honduras":
    print(diccionario.get("Honduras"))
elif pais == "Nicarag.getua":
    print(diccionario("Nicaragua"))
elif pais == "Costa Rica":
    print(diccionario.get("Costa Rica"))
elif pais == "Panama":
    print(diccionario.get("Panama"))
elif pais == "Argentina":
    print(diccionario.get("Argentina"))
elif pais == "Colombia":
    print(diccionario.get("Colombia"))
elif pais == "Venezuela":
    print(diccionario.get("Venezuela"))
elif pais == "España":
    print(diccionario.get("España"))
else:
    print("Pais no encontrado")





# Solución 2

diccionario2 = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Tegucigalpa",
"Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Ciudad Panama", "Argentina": "Buenos Aires", 
"Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Ingrese un pais: ")
# cambiar la primera letra a mayúscula
letra = pais.capitalize() in diccionario2

# este if es redundante
# otra opcion es: if letra:
if letra == True:
    print(diccionario2[pais.capitalize()])
else:
    print("Pais no encontrtado")





# solución 3

diccionario3 = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Tegucigalpa",
"Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", 
"Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Ingrese un país: ")

if pais.capitalize() in diccionario:
    print(diccionario[pais.capitalize()])
else:
    print("Pais no encontrado")


# solución 4 agregando el método title para cambiar la primera letra de cada palabra a mayúscula

diccionario4 = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Tegucigalpa",
"Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", 
"Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais = input("Ingrese un país: ")

if pais.title() in diccionario4:
    print(diccionario4[pais.title()])
else:
    print("País no encontrado") 



